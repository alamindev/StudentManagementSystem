import urllib
import json
import requests
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm,StudentRegistrationForm, StudentPresentForm
from .models import Student
from django.db.models import Q 
# Create your views here.
from .decorators import check_recaptcha
from django.contrib import messages
from django.conf import settings 

 

def index(request):
    return render(request, "index.html")
 
def logout_view(request):
    logout(request)
    return redirect('/')
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password= form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)  
    context = {
        "form":form 
    }    
    return render(request, "form.html", context)
def search(request):
    Roll = Student.objects.all()

    try:
        q = request.GET.get('q')
    except:
        q = None 
    if q:
        Roll = Student.objects.filter(Roll__contains=q)
        context = {'query':q, 'Roll':Roll}
        template = 'result.html'
    else:
        template = 'index.html'
        context = {}         
     
    return render(request, template, context)

def dashboardView(request):

    return render(request, "dashboard.html")

def registerView(request):
    form = StudentRegistrationForm(request.POST or None)
    if form. is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        return redirect("/")
    context = {
        'form':form,
        

    }   
    return render(request, "register.html", context)

def Student_Record(request):
    Record = Student.objects.all()

    return render(request, "Record.html", {"Record":Record})
def Student_Update(request, pid):
    post = get_object_or_404(Student, id=pid)
    form = StudentRegistrationForm(request.POST or None, request.FILES or None, instance=post )
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        return redirect("/")
    context ={
        "form":form
    }    

    return render(request, "register.html", context)
def Student_Delete(request, pid):
    post = get_object_or_404(Student, id=pid)
    post.delete()
    return redirect('index')
    
@check_recaptcha
def Student_Present(request):
    form = StudentPresentForm(request.POST or None)
    if form.is_valid() and request.recaptcha_is_valid:
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request, 'New comment added with success!')
        return redirect("index")
    context = {
        "form":form
    }    
    return render(request, "Present.html",context)




    

