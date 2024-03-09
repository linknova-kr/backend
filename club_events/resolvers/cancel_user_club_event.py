from graphene import ID, NonNull, Union, Mutation, InputObjectType
from graphql_jwt.decorators import login_required

from schema.types import NotFoundException, MutationError
from club_events.models import ClubEvent, UserClubEvent
from .join_club_event import UserClubEventType
import datetime

class CancelUserClubEventInput(InputObjectType):
  club_event_id = NonNull(ID)

class CancelUserClubEventResult(Union):
  class Meta:
    types = (UserClubEventType, NotFoundException, MutationError)

class CancelUserClubEvent(Mutation):
  class Arguments:
    input = NonNull(CancelUserClubEventInput)
  
  Output = NonNull(CancelUserClubEventResult)

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
    ).last  ()
    if user_club_event is None:
      return MutationError(reason='가입하지 않은 별모임입니다.')
    if user_club_event.member_id != user_id:
      return MutationError(reason='탈퇴 권한이 없습니다.')
    if user_club_event.cancelled_at is not None:
      return MutationError(reason='이미 탈퇴한 별모임입니다.')
    user_club_event.cancelled_at = datetime.datetime.now()
    user_club_event.save()
    return user_club_event