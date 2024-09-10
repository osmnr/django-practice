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
    readAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.messageId}-{self.read_userId}"
    


class ContactMessageReplies(models.Model):
    contactMessageId = models.ForeignKey(contactMessage,on_delete=models.CASCADE)
    isClient = models.BooleanField()
    replyUserId = models.ForeignKey(User,on_delete=models.PROTECT, null=True, blank=True)
    replyMessage = models.TextField()
    replyDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contactMessageId.subject}__{self.replyDate}"
    

class ContactMessageToken(models.Model):
    messageId = models.ForeignKey(contactMessage,on_delete=models.CASCADE)
    token = models.CharField(max_length=20, unique=True)
    expiryDate = models.DateTimeField()

    def __str__(self):
        return self.token
