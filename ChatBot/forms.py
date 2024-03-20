from django import forms
from ChatBot.models import ChatBot

class ChatBotForm(forms.ModelForm):
    class Meta:
        model=ChatBot
        fields=["prompt"]
