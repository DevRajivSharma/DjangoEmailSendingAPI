from django.urls import path
from .views import *
urlpatterns = [
    path('email_api',send_email,name='send_email'),
    path('',home)
]