from django.shortcuts import render

# Create your views here.

def bug(request):
    return render(request, 'bug/index.html')