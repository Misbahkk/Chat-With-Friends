from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('friend/<str:pk>', views.detail, name='detail'),
    path('sent_msg/<str:pk>', views.sentMessage, name='sent_msg'),
    path('rec_msg/<str:pk>', views.recivedMessage, name='rec_msg'),
    path('notification', views.chatNotification, name='notification'),

]
