from django.shortcuts import render
from .models import standard,ecommlite,ecommpro
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.contrib import messages,auth



from tkinter import E
from math import log

# Create your views here.
def index(request):
    return render(request,'homeapp/index.html')

def standard(request):
     if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        mob_number=request.POST.get('mob_number')
        message=request.POST.get('message')
        user_obj=standard.objects.create(first_name=first_name, last_name=last_name, email=email, mob_number=mob_number,message=message)
        user_obj.save()
        messages.success(request,"An email has been sent on your mail.")
        return HttpResponseRedirect(request.path_info)
     return render(request,'homeapp/standard.html')

def e_commlite(request):
    return render(request,'homeapp/ecommlite.html')

def e_commpro(request):
    return render(request,'homeapp/ecommpro.html')