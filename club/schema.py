from graphene import ID, Field, List, NonNull, ObjectType, Schema, Union
from graphene_django import DjangoObjectType

from schema.types import NotFoundException

from .models import Club


class ClubType(DjangoObjectType):
    class Meta:
        model = Club
        name = 'Club'

class ClubDetail(Union):
    class Meta:
        types = (ClubType, NotFoundException)

class Query(ObjectType):
    clubs = NonNull(List(NonNull(ClubType)))
    club = Field(NonNull(ClubDetail), id=NonNull(ID))

    def resolve_clubs(self, info, **kwargs):
        return Club.objects.all()
    
    def resolve_club(self, info, id):
        club = Club.objects.filter(id=id).first()
        if club is None:
            return NotFoundException(message=f'Club with id {id} does not exist')
        return club
    
club_schema = Schema(query=Query)