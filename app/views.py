"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.generic import ListView, DetailView
from app.models import User_mod, Reports
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import Signup, sign_up_acc, report2
#from django.views.decorators.csrf import csrf_exempt

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from twilio.rest import TwilioRestClient





def signup(request):
    if request.method == 'POST':
        user_form = Signup(data=request.POST)
        profile_form = sign_up_acc(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return HttpResponseRedirect('/login/')
        else:
            error = "Please fill out all the fields"
            return render(request, 'app/error.html')
    else:
        user_form = Signup()
        profile_form = sign_up_acc()
        return render(request, "app/sign.html", {'form': user_form, 'form2': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse('Your account is disabled. Please activate it')
        else:
            return HttpResponse("Login Failed, please check your username and password")
    else:
        return render(request, 'app/login.html')

@login_required
def index(request):
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'app/index.html', {'obj': username})

@login_required
def report(request):
    if request.user.is_authenticated():
        username = request.user.username
        li = Reports.objects.filter(user=request.user)
    return render(request, 'app/reports.html', {'obj': username, 'lis': li})

@login_required
def form(request):
    if request.method == 'POST':
        user_form = report2(data=request.POST)
        if user_form.is_valid():
            profile = user_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect('/showreport/')
        else:
            error = "Please fill out all the fields"
            return render(request, 'app/index.html')
    else:
        repor = report2()
        return render(request, 'app/form.html', {'form': repor})

def marketplace(request):
    items = Reports.objects.exclude(id1=0)
    return render(request, 'app/market.html', {'list':items})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')

@twilio_view
def sms(request):
    account_sid = "AC9c93b746c4637134e3f90ecef936e44c"
    auth_token = "884466a72597c7feeca762c22e4cbeb2"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to="+12535088701", from_="+12532143686",
                                     body="Hello there!")
    
    return HttpResponseRedirect('/login/')

def contact(request):
  return render(request, 'app/contact.html')


