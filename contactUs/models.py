from django.db import models


# Create your models here.
class contactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject