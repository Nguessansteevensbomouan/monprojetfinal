from django.urls import path
from .views import trombinoscope

urlpatterns = [
    path('trombinoscope/', trombinoscope, name='trombinoscope'),
]
