from django.urls import path
from . import views

app_name = 'contactUs'

urlpatterns = [
   path('', views.contactUs, name='contactUs'),
   path('list/', views.contactList, name='contactList'),
   path('detail/<int:id>/', views.contactUsDetail, name='contactUsDetail'),
   path('reply/<str:token>/<int:msgId>/',views.contactUsReply, name='contactUsReply'),
]