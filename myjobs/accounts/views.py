from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import employee
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def home(request):
    return render(request,'accounts/dashboard.html ')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', { 'form': form}) 
    
def emform(request):
   
    return render(request, 'emform.html')

def list(request):
   if request.method == "POST":
    Name = request.POST.get('Name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    occupation = request.POST.get('occupation')
    experience = request.POST.get('experience')
    return render(request, 'accounts/emform.html')
   en = employee(Name=Name,phone=phone,email=email,address=address,occupation=occupation,experience=experience)
   en.save()

def customer(request):
    return HttpResponse('Customer page')
 
# Create your views here.
...

