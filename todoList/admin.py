from django.contrib import admin
from .models import Todolist, UsersTodoList

class TodolistAdmin(admin.ModelAdmin):
    list_display = ('id', 'taskName', 'updatedDate','isDone','isDeleted')
    readonly_fields = ('updatedDate',)
    list_display_links = ('id', 'taskName', 'updatedDate','isDone','isDeleted')

# Register your models here.
admin.site.register(Todolist, TodolistAdmin)
admin.site.register(UsersTodoList)