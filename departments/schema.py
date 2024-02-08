import graphene
from graphene_django import DjangoObjectType
from .models import Department

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        name = 'Department'

class Query(graphene.ObjectType):
    departments = graphene.NonNull(graphene.List(graphene.NonNull(DepartmentType)))

    def resolve_departments(self, info, **kwargs):
        return Department.objects.all()
    
department_schema = graphene.Schema(query=Query)