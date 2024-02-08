from django.db import models
from groups.models import Group

class GroupSeason(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  class Meta:
    verbose_name = '모임 시즌'
    verbose_name_plural = '모임 시즌'