import graphene
from departments.schema import department_schema
from groups.schema import group_schema

class Query(department_schema.Query, group_schema.Query):
    pass

schema = graphene.Schema(query=Query)
