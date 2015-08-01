from django.core.management.base import BaseCommand, CommandError
import requests
from ...models import Team
import json
import time

class Command(BaseCommand):
  help = 'Requests daily update from the team members'
  def handle(self, *args, **options):
    for team in Team.objects.all().prefetch_related('workers'):
      for worker in team.workers.all():
        payload = {
          "text": "It's time for your daily update. Just give me a sentence or two to sync up with the team.",
          "channel": worker.username
        }
        r = requests.post(team.webhook_url, data=json.dumps(payload))
        time.sleep(2)