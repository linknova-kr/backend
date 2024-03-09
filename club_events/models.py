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
  
class UserClubEvent(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  club_event = models.ForeignKey(ClubEvent, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  cancelled_at = models.DateTimeField(null=True, blank=True)

  class Meta:
    verbose_name = '회원별 별모임 이벤트'
    verbose_name_plural = '회원별 별모임 이벤트'

  def __str__(self):
    return f"{self.club_event}: {self.member}"