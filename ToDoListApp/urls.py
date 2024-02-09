from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='ToDoList' ),
    path('office',views.office_work,name='office' ),
    path('physical',views.physical,name='physical' ),
]