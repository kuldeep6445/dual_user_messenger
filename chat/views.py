from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



def login_user1(request):
    a = authenticate(request,username='kuldeep',password='kuldeep')
    login(request,a)
    return redirect('/../')

def login_user2(request):
    a = authenticate(request,username='kunal',password='kunal')
    login(request,a)
    return redirect('/../')

def logout_request(request):
    logout(request)
    return redirect('/../../')

def check_login(request):
    if request.user.is_authenticated:
        return redirect('chatroom/')
    else:
        return render(request,'chat/login.html')



def chatroom(request):
    a = request.user
    context = {"user":a.username}
    return render(request,'chat/room.html',context)
