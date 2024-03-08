import graphene

class NotFoundException(graphene.ObjectType):
    message = graphene.String()

class MutationError(graphene.ObjectType):
    reason = graphene.String()