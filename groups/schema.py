from graphene import ID, Field, List, NonNull, ObjectType, Schema, Union
from graphene_django import DjangoObjectType

from schema.types import NotFoundException

from .models import Group


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        name = 'Group'

class GroupDetail(Union):
    class Meta:
        types = (GroupType, NotFoundException)

class Query(ObjectType):
    groups = NonNull(List(NonNull(GroupType)))
    group = Field(NonNull(GroupDetail), id=NonNull(ID))

    def resolve_groups(self, info, **kwargs):
        return Group.objects.all()
    
    def resolve_group(self, info, id):
        group = Group.objects.filter(id=id).first()
        if group is None:
            return NotFoundException(message=f'Group with id {id} does not exist')
        return group
    
group_schema = Schema(query=Query)