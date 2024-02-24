from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import CheckList
from .forms import CheckListForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def checklist(request):
    # return HttpResponse('welcome to checkList')
    if request.method =="POST":
        form = CheckListForm(request.POST or None)
        if form.is_valid:
            instance= form.save(commit=False)
            instance.manage=request.user
            instance.save()
        return redirect('checklist')
    else:
        # task = CheckListForm()
        # return render(request, 'checklist.html', {'tasks': task})
        task = CheckList.objects.filter(manage=request.user)
        context = {'welcome_text':'welcome to checklist','tasks':task}
        return render(request,'checklist.html',context)
    
@login_required    
def del_checklist(request,task_id):
    task= CheckList.objects.get(pk=task_id)
    task.delete()
    return redirect('checklist')

@login_required    
def mark_completed(request,task_id):
    try:
        task= CheckList.objects.get(pk=task_id)
        form =CheckListForm(request.POST or None ,instance=task)
        task.completed=True
        if form.is_valid:
            form.save()
    except:
        return redirect('checklist')
    return redirect('checklist')

def not_completed(request,task_id):
    try:
        task= CheckList.objects.get(pk=task_id)
        
        form =CheckListForm(request.POST or None ,instance=task)
        task.completed=False
        if form.is_valid:
            form.save()
    except:
        return redirect('checklist')
    return redirect('checklist')
