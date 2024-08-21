from django.urls import path
from . import views

app_name = 'contactUs'

urlpatterns = [
   path('', views.contactUs, name='contactUs'),
]