from django.urls import path
from . import views

app_name = 'todoList'

urlpatterns = [
    path('', views.todoList, name = 'index'),
    path('<int:pk>/update/', views.updateTodoItem, name = 'update' ),
    path('<int:xxx>/delete/', views.deletedTodoItem, name = 'delete' ),
]