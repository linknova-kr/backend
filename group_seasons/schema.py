import graphene
from graphene_django import DjangoObjectType
from .models import GroupSeason

class GroupSeasonType(DjangoObjectType):
    class Meta:
        model = GroupSeason
        name = 'GroupSeason'

class Query(graphene.ObjectType):
    groupSeasons = graphene.NonNull(graphene.List(graphene.NonNull(GroupSeasonType)))

    def resolve_groupSeasons(self, info, **kwargs):
        return GroupSeason.objects.all()
    
group_season_schema = graphene.Schema(query=Query)