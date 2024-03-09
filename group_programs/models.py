from django.db import models
from groups.models import Group
from member.models import Member

GROUP_PROGRAM_TYPE = (
  ('BOOK_FREE', '책: 자유책'),
  ('BOOK_LOUNGING', '책: 라운징'),
  ('BOOK_DESIGNATED', '책: 지정책'),
  ('ENGLISH', '영어'),
)

class GroupProgram(models.Model):
  title = models.CharField(max_length=100)
  type = models.CharField(max_length=20, choices=GROUP_PROGRAM_TYPE, default='BOOK_FREE')
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  host_member = models.ForeignKey(Member, on_delete=models.CASCADE)
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  class Meta:
    verbose_name = '모임 프로그램'
    verbose_name_plural = '모임 프로그램'

  def __str__(self):
    return self.title

USER_GROUP_PROGRAM_STATUS = (
  ('ABSENCE', '결석'),
  ('ATTENDANCE_NOTLATE', '출석: 지각안함'),
  ('ATTENDANCE_LATE', '출석: 지각'),
  ('PENDING', '미정'),
)

class UserGroupProgram(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  group_program = models.ForeignKey(GroupProgram, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  cancelled_at = models.DateTimeField(null=True)
  status = models.CharField(max_length=20, choices=USER_GROUP_PROGRAM_STATUS)

  class Meta:
    verbose_name = '회원별 모임 프로그램'
    verbose_name_plural = '회원별 모임 프로그램'

  def __str__(self):
    return f'{self.group_program}: {self.member}'