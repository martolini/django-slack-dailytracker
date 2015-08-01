from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import DailyUpdateForm

@csrf_exempt
def handle_command(request):
  if request.POST:
    form = DailyUpdateForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse("Added your daily update! Thanks :-)")
    else:
      return HttpResponse("Could not add your update. Make sure the update is more than 3 characters.")
  return HttpResponse("Say whaat?")
