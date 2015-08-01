from django import forms
from .models import Team, Worker, DailyUpdate

class DailyUpdateForm(forms.Form):
  team_id = forms.CharField()
  team_domain = forms.CharField()
  user_id = forms.CharField()
  user_name = forms.CharField()
  command = forms.CharField()
  text = forms.CharField()

  def is_valid(self):
    valid = super(DailyUpdateForm, self).is_valid()
    if not valid:
      return False
    if self.cleaned_data['command'] != '/dailyupdate':
      return False
    if len(self.cleaned_data['text']) < 3:
      return False
    try:
      team = Team.objects.get(id=self.cleaned_data['team_id'])
    except Team.DoesNotExist:
      team = Team.objects.create(id=self.cleaned_data['team_id'], name=self.cleaned_data['team_domain'])
    try:
      worker = Worker.objects.get(id=self.cleaned_data['user_id'])
    except Worker.DoesNotExist:
      worker = Worker.objects.create(id=self.cleaned_data['user_id'], name=self.cleaned_data['user_name'], team_id=self.cleaned_data['team_id'])
    return True

  def save(self):
    d = DailyUpdate.objects.create(
      worker_id=self.cleaned_data['user_id'],
      text=self.cleaned_data['text']
    )
    return d


