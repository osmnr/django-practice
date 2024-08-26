from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    


class MessageReadByUser(models.Model):
    messageId = models.ForeignKey(contactMessage,on_delete=models.CASCADE)
    read_userId = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.messageId}-{self.read_userId}"
    