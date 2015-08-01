from django.contrib import admin
from .models import Team, Worker, DailyUpdate

@admin.register(Team, Worker)
class TeamAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(DailyUpdate)
class DailyUpdateAdmin(admin.ModelAdmin):
  list_display = ('worker', 'created_at')