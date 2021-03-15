from django.shortcuts import  render , redirect
from django.urls import path
from . import views

urlpatterns=[
    path('',views.normal_view),
    path('admin/',views.admin_view),
]