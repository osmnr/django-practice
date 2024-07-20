from django.urls import path
from . import views

app_name = 'todoList'

urlpatterns = [
    path('', views.todoList, name = 'todoList'),
]