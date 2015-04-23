from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Peer_Eval.forms import *
from Peer_Eval.models import *

def splash(request):
    return render(request, "splash.html")


@login_required(login_url="/")
def home(request):
    return render(request, "index.html")

@login_required(login_url="/")
def submitted(request):
    cur_user = request.user
    survey = project.objects.filter(members__name__in=[cur_user], enddate__lt=datetime.now())

    return render(request, "completed_surveys.html", {'survey':survey})

@login_required(login_url="/")
def available(request):
    cur_user = request.user
    # cur_user = str(cur_user)
    survey = project.objects.filter(members__in=[cur_user], enddate__gte=datetime.now())
    # print survey.__len__()

    return render(request, "Available_Surveys.html", {'survey':survey})


def log_in(request):
    error = ""
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        error = "Username or Password invalid."
    return render(request, "login.html", {'error' :error} )

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")

def create_user(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form=UserForm()
    return render(request, "create_user.html", {'form': form})
    
def base(request):
    return render(request, "base.html")
