from django.conf.urls import url

from django.conf import settings
from views import handle_command

urlpatterns = [
  url(r'^$', handle_command),
]