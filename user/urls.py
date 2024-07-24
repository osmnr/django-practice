from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.userLogin, name = 'userLogin'),
    path('register/', views.userRegister, name = 'userRegister'),
    path('logout/', views.userLogout, name = 'userLogout'),
]