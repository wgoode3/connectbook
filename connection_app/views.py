from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})

def user(request):
    User.objects.add_user(request.POST)
    return redirect("/")

def connect(request):
    User.objects.connect(request.POST)
    return redirect("/")