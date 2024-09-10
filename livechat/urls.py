from django.urls import path
from . import views

app_name = 'livechat'

urlpatterns = [
   path('', views.livechat, name='livechat'), 
]