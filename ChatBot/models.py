from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatBot(models.Model):
    manage = models.ForeignKey(User,on_delete=models.CASCADE,  default=None)
    prompt = models.TextField()
    
    def __str__(self):
        return self.prompt
    
    

    
