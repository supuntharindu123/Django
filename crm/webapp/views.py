from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import createuserform,loginform,NameForm,CreateRecord,UpdateRecord

# for login
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

# Create your views here.
def home(request):
    return render(request,'webapp/index.html')

def register (request):
    form=createuserform()
    if request.method == 'POST':
        form=createuserform(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Registration successfully")
            return redirect("mylogin")
        
    context={
        'form': form,
    }
    return render(request,'webapp/register.html',context=context)


def getname(request):

    if request.method == "POST":
   
        form = NameForm(request.POST)
  
        if form.is_valid():
         
            return HttpResponse("Success")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    context={
        'form': form,
    }
    return render(request,'webapp/register2.html',context=context)


def mylogin(request):
    form=loginform()

    if request.method == 'POST':
        form=loginform(request, data=request.POST)
 
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request,"Login successfully")
                return redirect('dashboard')

    context={
        'form':form,
    }
    return render(request,'webapp/login.html',context=context)


def mylogout(request):
    auth.logout(request)  
    messages.success(request,"Logout successfully")
    return redirect('mylogin')   



@login_required(login_url="mylogin")
def dashboard(request):

    my_records=Record.objects.all()
    context={
        'records':my_records,  
    }
    return render(request,'webapp/dash.html',context=context)

@login_required(login_url='mylogin')
def createrecord(request):
    form =CreateRecord()

    if request.method == 'POST':
        form = CreateRecord(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Record created successfully")
            return redirect('dashboard')
        
    context={
        'form': form,
    }
    return render(request,'webapp/create-record.html',context=context)



@login_required(login_url='mylogin')
def updateRecord(request,pk):
    record=Record.objects.get(id=pk)
    form=UpdateRecord(instance=record)

    if(request.method == 'POST'):
        form=UpdateRecord(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully")
            return redirect('dashboard')
        
    context={
        'form': form,
    }
    return render(request,'webapp/update-record.html',context=context)


@login_required(login_url='mylogin')
def viewRecord(request,pk):
    record=Record.objects.get(id=pk)
    context={
       'record':record,
    }
    return render(request,'webapp/view-record.html',context=context)


@login_required(login_url='mylogin')

def deleteRecord(request,pk):
    record=Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Record deleted successfully")
    return redirect('dashboard')