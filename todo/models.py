from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=100,blank=True,default='')
    deadline = models.DateTimeField(default=datetime.now, blank=True)
    done = models.BooleanField(default=False)
    priority = models.CharField(choices=[('low','low'),('normal','normal'),('high','high')],default='normal',max_length=100)
    tags = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering=['deadline']