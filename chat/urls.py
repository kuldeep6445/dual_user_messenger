from django.shortcuts import  render , redirect
from django.urls import path
from . import views

urlpatterns=[
    path('',views.check_login),
    path('user1/',views.login_user1),
    path('user2/',views.login_user2),
    path('chatroom/',views.chatroom),
    path('chatroom/logout/',views.logout_request),
]