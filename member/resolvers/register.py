from django.contrib.auth import get_user_model
from graphene import (Enum, InputObjectType, Mutation,
                      NonNull, ObjectType, String, Union)
from graphql_jwt.shortcuts import create_refresh_token, get_token

from member.models import GENDER
from schema.types import MutationError

class RegisterInput(InputObjectType):
    identifier = NonNull(String)
    name = NonNull(String)
    birth_date = NonNull(String)
    gender = NonNull(Enum('Gender', GENDER))
    email = String
    phone_number = NonNull(String)
    password = NonNull(String)


class RegisterSuccess(ObjectType):
    token = String()
    refresh_token = String()

class RegisterResult(Union):
    class Meta:
        types = (RegisterSuccess, MutationError)


class Register(Mutation):
    class Arguments:
        input = NonNull(RegisterInput)

    Output = NonNull(RegisterResult)

    def mutate(self, info, input):
        model = get_user_model()
        identifier = input.identifier
        existing = model.objects.filter(identifier=identifier)
        if existing.exists():
            return MutationError(reason='이미 존재하는 식별자입니다.')
        user = model.objects.create_user(**input)
        user.set_password(input.password)
        user.save()
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return RegisterSuccess(token=token, refresh_token=refresh_token)