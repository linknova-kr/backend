from django.contrib import admin
from .models import ClubEvent, UserClubEvent

admin.site.register(ClubEvent)
admin.site.register(UserClubEvent)