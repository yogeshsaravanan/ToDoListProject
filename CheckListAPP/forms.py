from django import forms
from CheckListAPP.models import CheckList

class CheckListForm(forms.ModelForm):
    class Meta:
        model=CheckList
        fields=["task","start_time","end_time","completed"]
