from graphene import ID, Field, List, NonNull, ObjectType, Schema, Union
from graphene_django import DjangoObjectType

from schema.types import NotFoundException

from .models import GroupProgram
from .resolvers.join_group_program import JoinGroupProgram

class GroupProgramType(DjangoObjectType):
  class Meta:
    model = GroupProgram
    name = 'GroupProgram'

class GroupProgramDetail(Union):
  class Meta:
    types = (GroupProgramType, NotFoundException)

class Query(ObjectType):
  groupPrograms = NonNull(List(NonNull(GroupProgramType)))
  groupProgram = Field(NonNull(GroupProgramDetail), id=NonNull(ID))

  def resolve_groupPrograms(self, info, **kwargs):
    return GroupProgram.objects.all()
  
  def resolve_groupProgram(self, info, id):
    groupProgram = GroupProgram.objects.filter(id=id).first()
    if groupProgram is None:
      return NotFoundException(message=f'GroupProgram with id {id} does not exist')
    return groupProgram
  
class Mutation(ObjectType):
  joinGroupProgram = JoinGroupProgram.Field()
  
group_program_schema = Schema(query=Query, mutation=Mutation)