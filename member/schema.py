from graphene import Field, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql_jwt import Refresh

from .models import Member
from .resolvers.login import Login
from .resolvers.register import Register


class MemberType(DjangoObjectType):
    class Meta:
        model = Member
        name = 'Member'
        exclude = ('password', 'is_superuser', 'last_login')

class Query(ObjectType):
    me = Field(MemberType)

    @login_required
    def resolve_me(self, info):
        return info.context.user

class Mutation(ObjectType):
    register = Register.Field()
    login = Login.Field()
    refresh_token = Refresh.Field()


member_schema = Schema(query=Query, mutation=Mutation)