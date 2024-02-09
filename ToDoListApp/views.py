from django.shortcuts import render
from django.http import HttpResponse
from ToDoListApp.models import ToDoList

# Create your views here.

def index(request):
    tasks = ToDoList.objects.all
    context = {'welcome_text':'welcome to to do list',"tasks":tasks}
    return render(request,'ToDoList.html',context)
    # return render(request,'ToDoList.html',)

def office_work(request):
    context = {'welcome_text':'welcome to office list'}
    return render(request,'office.html',context)

def physical(request):
    context = {'welcome_text':'welcome to physical list'}
    return render(request,'physical.html',context)