from django.db import models

# Create your models here.
class Category(models.Model):
    ctgName = models.CharField(unique=True, max_length=80)
    ctgImage = models.ImageField(upload_to='home/images/')
    ctgURL = models.CharField(unique=True, max_length=80)
    isActive = models.BooleanField()

    def __str__(self):
        return self.ctgName
    

