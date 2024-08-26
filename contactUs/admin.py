from django.contrib import admin
from .models import contactMessage, MessageReadByUser


# Register your models here.
admin.site.register(contactMessage)
admin.site.register(MessageReadByUser)