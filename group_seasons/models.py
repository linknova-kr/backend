from django.db import models
from groups.models import Group
from member.models import Member

class GroupSeason(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  class Meta:
    verbose_name = '모임 시즌'
    verbose_name_plural = '모임 시즌'

USER_GROUP_SEASON_LEVEL = (
  ('INACTIVE', '휴면'),
  ('WAITING_DEPOSIT', '입금대기'),
  ('ACTIVE', '활동중'),
  ('SUPER', '슈퍼회원')
)

class UserGroupSeason(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  group_season = models.ForeignKey(GroupSeason, on_delete=models.CASCADE)
  level = models.CharField(max_length=20, choices=USER_GROUP_SEASON_LEVEL, default='INACTIVE')
  completed = models.BooleanField(default=False)
  
  class Meta:
    verbose_name = '회원별 모임 시즌'
    verbose_name_plural = '회원별 모임 시즌'