from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_service import authe


def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"Home.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")
 
def signUp(request):
    return render(request,"Registration.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "Registration.html")
     return render(request,"Login.html")