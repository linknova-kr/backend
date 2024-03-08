from django.contrib.auth import get_user_model
from graphene import (InputObjectType, Mutation, NonNull, ObjectType, String,
                      Union)
from graphql_jwt.shortcuts import create_refresh_token, get_token

from schema.types import MutationError


class LoginInput(InputObjectType):
    identifier = NonNull(String)
    password = NonNull(String)

class LoginSuccess(ObjectType):
    token = String()
    refresh_token = String()

class LoginResult(Union):
    class Meta:
        types = (LoginSuccess, MutationError)

class Login(Mutation):
    class Arguments:
        input = NonNull(LoginInput)

    Output = NonNull(LoginResult)

    def mutate(self, info, input):
        model = get_user_model()
        identifier = input.identifier
        password = input.password
        user = model.objects.filter(identifier=identifier).first()
        if user is None:
            return MutationError(reason='존재하지 않는 식별자입니다.')
        if not user.check_password(password):
            return MutationError(reason='잘못된 비밀번호입니다.')
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return LoginSuccess(token=token, refresh_token=refresh_token)
