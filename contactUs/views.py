from django.shortcuts import render
from .models import contactMessage
from django.contrib import messages
# Create your views here.


def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if len(subject) <= 180 and len(subject) >= 5 and len(name) <= 200 and len(name) >= 3:
            try:
                a = contactMessage(name=name, email=email, subject=subject, message=message)
                a.save()
                messages.success(request, 'Thank you for contacting us! Your message has been received!')
            except contactMessage.DoesNotExist:
                messages.error(request, 'Invalid entry')
        else:
            messages.error(request, "Invalid Entry")
    return render(request,"contactUs/contact.html")



