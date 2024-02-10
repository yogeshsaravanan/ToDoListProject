from django import forms
from ToDoListApp.models import ToDoList

class ToDoListForm(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=["task","assignee","status","ETA","risk_flag"]
