import graphene
from graphene_django import DjangoObjectType
from .models import Group

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        name = 'Group'

class Query(graphene.ObjectType):
    groups = graphene.NonNull(graphene.List(graphene.NonNull(GroupType)))

    def resolve_groups(self, info, **kwargs):
        return Group.objects.all()
    
group_schema = graphene.Schema(query=Query)