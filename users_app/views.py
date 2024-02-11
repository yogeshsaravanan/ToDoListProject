from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from users_app.forms import CustomUserCreation

def register(request):
    if request.method =="POST":
        form = CustomUserCreation(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,("User Registerd Successfully!"))    
        return redirect('register')
    else:
        register_form = CustomUserCreation()
    return render(request,'register.html',{'register_form':register_form})
