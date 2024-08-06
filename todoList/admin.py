from django.contrib import admin
from .models import UsersTodoList


class UsersTodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sessionKey', 'taskName', 'updatedDate', 'isDone','isDeleted' )


# Register your models here.
admin.site.register(UsersTodoList,UsersTodoListAdmin)