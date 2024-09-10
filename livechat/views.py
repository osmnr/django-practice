from django.shortcuts import render
# Create your views here.


def livechat(request):
    
    return render(request, 'livechat/livechat.html')