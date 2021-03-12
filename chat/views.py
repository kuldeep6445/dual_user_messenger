from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
import pymongo ,dns 
    
client = pymongo.MongoClient("mongodb+srv://KSB:kuldeep@cluster0.gfqd2.mongodb.net/test?retryWrites=true&w=majority")
db = client['test']


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

def get_last_srno():
    col = db['chat_dual']

def update_mssage_to_db(text1 , request):
    col = db['chat_dual']
    num = get_last_srno()
    dic = {'srno':'1'}

def chatroom(request):
    text1 = request.POST.get('sent_mssg','')
    update_mssage_to_db(text1,request)
    a = request.user
    context = {"user":a.username}
    return render(request,'chat/room.html',context)
