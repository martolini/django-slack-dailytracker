from django.core.management.base import BaseCommand, CommandError
import requests
import json
from ...models import Team, DailyUpdate
from django.utils import timezone
import re
from datetime import timedelta
import time

class Command(BaseCommand):
  help = 'Give out summary'
  def handle(self, *args, **options):
    for team in Team.objects.all().prefetch_related('workers'):
      text = ''
      for worker in team.workers.all():
        try:
          latest = worker.dailyupdates.latest('created_at')
        except DailyUpdate.DoesNotExist:
          continue
        if latest.created_at > timezone.now() - timedelta(hours=23):
          text += '\r\n\r\n{} {}'.format(worker.username, latest.text)
      if text:
        payload = {
          "text": 'Today\'s daily update{}'.format(re.sub('(@\w+)', lambda m: '<{}>'.format(m.group(1)), text)),
          "channel": team.channel
        }
        requests.post(team.webhook_url, data=json.dumps(payload))
        time.sleep(2)



