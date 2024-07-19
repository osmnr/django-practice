from django.shortcuts import render
from .models import Category

# Create your views here.


def home(request):
    categoryList = Category.objects.all()
    data = {
        'categoryList':categoryList
    }
    return render(request, 'home/index.html', data)