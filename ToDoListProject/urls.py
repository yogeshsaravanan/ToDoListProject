from django.contrib import admin
from django.urls import path,include
from ToDoListApp import views as todolistapp_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolistapp_view.index,name='index' ),
    path('account/',include("users_app.urls")),
    path('ToDoList/',include("ToDoListApp.urls")),
    path('office',todolistapp_view.office_work,name='office' ),
    path('physical',todolistapp_view.physical,name='physical' )
]
