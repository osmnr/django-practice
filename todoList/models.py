from django.db import models

# Create your models here.

class Todolist(models.Model):
    taskName = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    updatedDate = models.DateField(auto_now=True)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.taskName
    

    