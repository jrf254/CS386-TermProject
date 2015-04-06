from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def splash(request):
    return render(request, "splash.html")

# @login_required(login_url="/")
def home(request):
    return render(request, "index.html")

def login(request):
    error = ""
    print(request.method)

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

def logout(request):
    logout(request)
    return HttpResponseRedirect("/")
