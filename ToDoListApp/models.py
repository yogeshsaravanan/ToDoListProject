from django.db import models

# Create your models here.
class ToDoList(models.Model):
    task = models.CharField(max_length=300)
    status_type = models.TextChoices("status_type", "TO_DO DEFINED IN_PROGRESS COMPLETED")
    status = models.CharField(blank=True, choices=status_type, max_length=20,default='TO_DO')
    assignee = models.CharField(max_length= 20)
    ETA = models.DateField()
    risk_flag = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task 
    
    