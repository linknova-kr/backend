from graphene import ID, NonNull, Union, Mutation, InputObjectType
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from schema.types import NotFoundException, MutationError
from club_events.models import ClubEvent, UserClubEvent

class UserClubEventType(DjangoObjectType):
  class Meta:
    model = UserClubEvent
    name = 'UserClubEvent'

class JoinClubEventInput(InputObjectType):
  club_event_id = NonNull(ID)

class JoinClubEventResult(Union):
  class Meta:
    types = (UserClubEventType, NotFoundException, MutationError)

class JoinClubEvent(Mutation):
  class Arguments:
    input = NonNull(JoinClubEventInput)
  
  Output = NonNull(JoinClubEventResult)

  @login_required
  def mutate(self, info, input):
    user_id = info.context.user.id
    club_event_id = input.club_event_id
    club_event = ClubEvent.objects.filter(id=club_event_id).first()
    if club_event is None:
      return NotFoundException(message=f'ClubEvent with id {club_event_id} does not exist')
    user_club_event = UserClubEvent.objects.filter(
      member_id=user_id, 
      club_event_id=club_event_id
    ).last()
    if user_club_event is not None and user_club_event.cancelled_at is None:
      return MutationError(reason='이미 가입된 별모임입니다.')
    user_club_event = UserClubEvent(
      member_id=user_id,
      club_event_id=club_event_id
    )
    user_club_event.save()
    return user_club_event