from django.db import models
from departments.models import Department

class Group(models.Model):
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  slug = models.CharField(max_length=40)
  name = models.CharField(max_length=40)

  class Meta:
    verbose_name = '모임'
    verbose_name_plural = '모임'