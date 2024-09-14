from django.contrib import admin
from .models import Bug, BugStatus, BugTransactionType, Comment
# Register your models here.


class BugStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

class BugAdmin(admin.ModelAdmin):
    list_display = ('id', 'bugTitle' )

class BugTransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'trxTypeText')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')



# Register your models here.
admin.site.register(Bug,BugAdmin)
admin.site.register(BugStatus,BugStatusAdmin)
admin.site.register(BugTransactionType,BugTransactionTypeAdmin)
admin.site.register(Comment,CommentAdmin)