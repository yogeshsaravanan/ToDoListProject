from django.shortcuts import render,redirect
from django.http import HttpResponse
from ToDoListApp.models import ToDoList
from ToDoListApp.forms import ToDoListForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def todolist(request):
    if request.method =="POST":
        form = ToDoListForm(request.POST or None)
        if form.is_valid:
            form.save()
        messages.success(request,("New Task Added!"))    
        return redirect('ToDoList')
    else:    
        tasks = ToDoList.objects.all()
        paginator =Paginator(tasks,5)
        page=request.GET.get('pg')
        tasks=paginator.get_page(page)
        
        context = {'welcome_text':'welcome to to do list',"tasks":tasks}
        return render(request,'ToDoList.html',context)
    # return render(request,'ToDoList.html',)
    
def delete_task(request,task_id):
    task= ToDoList.objects.get(pk=task_id)
    task.delete()
    return redirect('ToDoList')

def edit_task(request,task_id):
    if request.method =="POST":
        task = ToDoList.objects.get(pk=task_id)
        form = ToDoListForm(request.POST or None , instance=task)
        if form.is_valid:
            form.save()
        messages.success(request,("New Task updated!"))    
        return redirect('ToDoList')
    else:    
        task = ToDoList.objects.get(pk=task_id)
        context = {'welcome_text':'welcome to to do list','task':task}
        return render(request,'edit.html',context)
 
def index(request):
    context = {'welcome_text':'welcome to Task Manager!'}
    return render(request,'index.html',context)    
    

def office_work(request):
    context = {'welcome_text':'welcome to office list'}
    return render(request,'office.html',context)

def physical(request):
    context = {'welcome_text':'welcome to physical list'}
    return render(request,'physical.html',context)