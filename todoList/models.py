from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todolist(models.Model):
    taskName = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    updatedDate = models.DateTimeField(auto_now=True)
    isDeleted = models.BooleanField(default=False)


    def __str__(self):
        return self.taskName
    

class UsersTodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    sessionKey = models.TextField()
    taskName = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    updatedDate = models.DateTimeField(auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.sessionKey