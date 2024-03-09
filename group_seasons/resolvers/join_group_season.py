from graphene import ID, NonNull, Union, Mutation, InputObjectType
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from schema.types import NotFoundException, MutationError

from group_seasons.models import GroupSeason, UserGroupSeason


class UserGroupSeasonType(DjangoObjectType):
    class Meta:
        model = UserGroupSeason
        name = 'UserGroupSeason'

class JoinGroupSeasonInput(InputObjectType):
    group_season_id = NonNull(ID)

class JoinGroupSeasonResult(Union):
    class Meta:
        types = (UserGroupSeasonType, NotFoundException, MutationError)

class JoinGroupSeason(Mutation):
    class Arguments:
        input = NonNull(JoinGroupSeasonInput)
    
    Output = NonNull(JoinGroupSeasonResult)

    @login_required
    def mutate(self, info, input):
        user_id = info.context.user.id
        group_season_id = input.group_season_id
        group_season = GroupSeason.objects.filter(id=group_season_id).first()
        if group_season is None:
            return NotFoundException(message=f'GroupSeason with id {group_season_id} does not exist')
        user_group_season = UserGroupSeason.objects.filter(
            member_id=user_id, 
            group_season_id=group_season_id
        ).first()
        if user_group_season is not None:
            return MutationError(reason='이미 가입된 모임입니다.')
        created = UserGroupSeason.objects.create(
            member_id=user_id, 
            group=group_season.group, 
            group_season_id=group_season_id, 
            level='INACTIVE', 
            completed=False,
        )
        return created