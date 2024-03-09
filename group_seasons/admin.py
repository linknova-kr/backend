from django.contrib import admin
from .models import GroupSeason, UserGroupSeason

admin.site.register(GroupSeason)
admin.site.register(UserGroupSeason)