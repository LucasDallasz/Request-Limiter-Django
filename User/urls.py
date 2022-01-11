from django.urls import path
from .views import *

app_name = 'User'

urlpatterns = [
    path('', user_login, name='login'),
    path('register/', user_register, name='register'),
]