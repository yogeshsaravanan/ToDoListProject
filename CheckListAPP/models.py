from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckList(models.Model):
    # manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    start_time= models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task 
    
    class Meta:
        ordering = ['id']
    