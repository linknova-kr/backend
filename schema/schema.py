import graphene
from club.schema import club_schema
from departments.schema import department_schema
from groups.schema import group_schema
from group_seasons.schema import group_season_schema

class Query(club_schema.Query, department_schema.Query, group_schema.Query, group_season_schema.Query):
    pass

schema = graphene.Schema(query=Query)
