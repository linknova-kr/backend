import graphene

class NotFoundException(graphene.ObjectType):
    message = graphene.String()