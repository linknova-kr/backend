from graphene import ID, Field, List, NonNull, ObjectType, Schema, Union
from graphene_django import DjangoObjectType

from schema.types import NotFoundException

from .models import GroupSeason


class GroupSeasonType(DjangoObjectType):
    class Meta:
        model = GroupSeason
        name = 'GroupSeason'

class GroupSeasonDetail(Union):
    class Meta:
        types = (GroupSeasonType, NotFoundException)

class Query(ObjectType):
    groupSeasons = NonNull(List(NonNull(GroupSeasonType)))
    groupSeason = Field(NonNull(GroupSeasonDetail), id=NonNull(ID))

    def resolve_groupSeasons(self, info, **kwargs):
        return GroupSeason.objects.all()
    
    def resolve_groupSeason(self, info, id):
        groupSeason = GroupSeason.objects.filter(id=id).first()
        if groupSeason is None:
            return NotFoundException(message=f'GroupSeason with id {id} does not exist')
        return groupSeason
    
group_season_schema = Schema(query=Query)