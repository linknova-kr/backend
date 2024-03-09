from graphene import ID, Field, List, NonNull, ObjectType, Schema, Union
from graphene_django import DjangoObjectType

from schema.types import NotFoundException
from .models import ClubEvent
from .resolvers.join_club_event import JoinClubEvent

class ClubEventType(DjangoObjectType):
  class Meta:
    model = ClubEvent
    name = 'ClubEvent'

class ClubEventDetail(Union):
  class Meta:
    types = (ClubEventType, NotFoundException)

class Query(ObjectType):
  clubEvents = NonNull(List(NonNull(ClubEventType)))
  clubEvent = Field(NonNull(ClubEventDetail), id=NonNull(ID))

  def resolve_clubEvents(self, info, **kwargs):
    return ClubEvent.objects.all()
  
  def resolve_clubEvent(self, info, id):
    clubEvent = ClubEvent.objects.filter(id=id).first()
    if clubEvent is None:
      return NotFoundException(message=f'ClubEvent with id {id} does not exist')
    return clubEvent

class Mutation(ObjectType):
  joinClubEvent = JoinClubEvent.Field() 

club_event_schema = Schema(query=Query, mutation=Mutation)