from django.contrib import admin
from .models import contactMessage, MessageReadByUser, ContactMessageReplies, ContactMessageToken


# Register your models here.
admin.site.register(contactMessage)
admin.site.register(MessageReadByUser)
admin.site.register(ContactMessageReplies)
admin.site.register(ContactMessageToken)
