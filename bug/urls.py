from django.urls import path
from . import views

app_name = 'bug'

urlpatterns = [
    path('', views.bug, name = 'bug'),
    path('detail/<int:id>', views.detail, name='detail'),
]