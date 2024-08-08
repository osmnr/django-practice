from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
   path('home/', views.home, name='home'),
]