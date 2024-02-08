import graphene
from departments.schema import department_schema

class Query(department_schema.Query):
    pass

schema = graphene.Schema(query=Query)
