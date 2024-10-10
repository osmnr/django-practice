from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('item/', views.item_api,name='item_api'),
]