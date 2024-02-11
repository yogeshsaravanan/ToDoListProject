from django.urls import path
from . import views

urlpatterns = [
    path('',views.todolist,name='ToDoList' ),
    path('delete/<task_id>',views.delete_task,name='delete_task' ),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
]