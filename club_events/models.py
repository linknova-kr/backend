from django.db import models

from club.models import Club
from member.models import Member

class ClubEvent(models.Model):
  club = models.ForeignKey(Club, on_delete=models.CASCADE)
  host_member = models.ForeignKey(Member, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  class Meta:
    verbose_name = '별모임 이벤트'
    verbose_name_plural = '별모임 이벤트'

  def __str__(self):
    return f"{self.club}: {self.title}"