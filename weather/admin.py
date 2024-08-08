from django.contrib import admin
from .models import City, UserCity


class CityAdmin(admin.ModelAdmin):
    list_display = ('name','id')


class UserCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'user')


# Register your models here.

admin.site.register(City, CityAdmin)
admin.site.register(UserCity, UserCityAdmin)


