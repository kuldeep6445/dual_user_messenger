from django.shortcuts import render ,redirect

def normal_view(request):
    return render(request,'chat/index.html')

def admin_view(request):
    return render(request,'chat/admin.html')
