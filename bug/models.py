from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BugStatus(models.Model):
    status = models.CharField(unique=True, max_length=80)


class Bug(models.Model):
    createdBy = models.ForeignKey(User, related_name='createdBy',  on_delete=models.CASCADE, null=True, blank=True)
    bugTitle = models.CharField(unique=True, max_length=80)
    taskStatus = models.ForeignKey(BugStatus,on_delete=models.CASCADE )
    taskContext = models.CharField( max_length=250)
    reportedAt = models.DateTimeField(auto_now_add=True)
    assignedTo = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.bugTitle

class BugTransactionType(models.Model):
    trxTypeName = models.IntegerField()
    trxTypeText = models.CharField(unique=True, max_length=80)
    
    def __str__(self):
        return self.trxTypeText
