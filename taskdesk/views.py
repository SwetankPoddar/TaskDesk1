from django.shortcuts import render

def user_login(request):
    return render(request,'taskdesk/login.html',{})
