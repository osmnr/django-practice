from django.contrib import admin
from .models import Bug, BugStatus, BugTransactionType
# Register your models here.


class BugStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

class BugAdmin(admin.ModelAdmin):
    list_display = ('id', 'bugTitle' )

class BugTransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'trxTypeText')

# Register your models here.
admin.site.register(Bug,BugAdmin)
admin.site.register(BugStatus,BugStatusAdmin)
admin.site.register(BugTransactionType,BugTransactionTypeAdmin)