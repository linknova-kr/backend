from django.db import models
from departments.models import Department

class Club(models.Model):
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  slug = models.CharField(max_length=40)
  name = models.CharField(max_length=40)

  class Meta:
    verbose_name = '별모임'
    verbose_name_plural = '별모임'