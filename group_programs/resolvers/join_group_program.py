from graphene import ID, NonNull, Union, Mutation, InputObjectType
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from schema.types import NotFoundException, MutationError
from group_programs.models import GroupProgram, UserGroupProgram
from group_seasons.models import UserGroupSeason, GroupSeason

class UserGroupProgramType(DjangoObjectType):
    class Meta:
        model = UserGroupProgram
        name = 'UserGroupProgram'

class JoinGroupProgramInput(InputObjectType):
    group_program_id = NonNull(ID)

class JoinGroupProgramResult(Union):
    class Meta:
        types = (UserGroupProgramType, NotFoundException, MutationError)

class JoinGroupProgram(Mutation):
    class Arguments:
        input = NonNull(JoinGroupProgramInput)
    
    Output = NonNull(JoinGroupProgramResult)

    @login_required
    def mutate(self, info, input):
        user_id = info.context.user.id
        print("YO!!", input)
        group_program_id = input.group_program_id
        group_program = GroupProgram.objects.filter(id=group_program_id).first()
        if group_program is None:
            return NotFoundException(message=f'GroupProgram with id {group_program_id} does not exist')
        print("GROUPPROGRAM", group_program)
        user_group_program = UserGroupProgram.objects.filter(
            member_id=user_id, 
            group_program_id=group_program_id
        ).first()
        print("USERGROU", user_group_program)
        if user_group_program is not None:
            return MutationError(reason='이미 가입된 모임입니다.')
        group_season = GroupSeason.objects.filter(
            group=group_program.group,
            # todo 현재 시즌을 찾기 위해 조건 추가 필요
        ).last()
        print("GROUPSEASON", group_season)
        user_group_season = UserGroupSeason.objects.filter(
            member_id=user_id, 
            group=group_program.group,
            group_season=group_season
        ).first()
        print("USERGROUPSEASON", user_group_season)
        if user_group_season is None:
            return MutationError(reason='모임에 가입되어있지 않습니다.')
        if user_group_season.level == 'INACTIVE':
            return MutationError(reason='모입 가입상태가 휴면중 입니다.')
        if user_group_season.level == 'WAITING_DEPOSIT':
            return MutationError(reason='입금대기중인 모임입니다.')

        created = UserGroupProgram.objects.create(
            member_id=user_id, 
            group_program_id=group_program_id, 
            status='PENDING',
        )
        return created