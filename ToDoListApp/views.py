from django.shortcuts import render,redirect
from django.http import HttpResponse
from ToDoListApp.models import ToDoList
from ToDoListApp.forms import ToDoListForm

# Create your views here.

def todolist(request):
    if request.method =="POST":
        form = ToDoListForm(request.POST or None)
        if form.is_valid:
            form.save()
        return redirect('ToDoList')
    else:    
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