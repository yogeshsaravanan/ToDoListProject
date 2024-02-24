from django.urls import path
from . import views

urlpatterns = [
    path('',views.checklist,name='checklist' ),
    path('delete/<task_id>',views.del_checklist,name='delete_checklist' ),
    path('complete/<task_id>',views.mark_completed,name='mark_completed' ), 
    path('notComplete/<task_id>',views.not_completed,name='mark_not_completed' ),
]