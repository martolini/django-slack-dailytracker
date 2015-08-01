from django.core.management.base import BaseCommand, CommandError
import requests
import json
from ...models import Team
from django.utils import timezone
from datetime import timedelta
import time

class Command(BaseCommand):
  help = 'Requests daily update from the team members'
  def handle(self, *args, **options):
    for team in Team.objects.all().prefetch_related('workers'):
      dunnedworkers = []
      fhoursago = timezone.now() - timedelta(hours=4)
      for worker in team.workers.all():
        if not worker.dailyupdates.filter(created_at__gte=fhoursago).exists():
          requests.post(team.webhook_url, data=json.dumps({
            "text": "You have not submitted your daily update yet, do it now or I'll assume you took the day off :-)",
            "channel": worker.username
          }))
        time.sleep(2)