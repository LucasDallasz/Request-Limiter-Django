from django.urls import path
from .views import *

app_name = 'request'

urlpatterns = [
    path('invalid_request/', invalid_request, name='invalid_request')
]