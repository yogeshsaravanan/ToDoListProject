from django.urls import path
from . import views

urlpatterns = [
    path('',views.todolist,name='ToDoList' ),
    path('office',views.office_work,name='office' ),
    path('physical',views.physical,name='physical' ),
]