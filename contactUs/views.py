from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import contactMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.


def contactUs(request):
    if request.method == 'POST':
        if request.user:
            name = request.user.username
            if request.user.email:
                email = request.user.email
            else:
                email = request.POST.get('email')
                ## saving the email to user table
                a = User.objects.get(pk=request.user.id)
                a.email =email
                a.save()
        else:
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



def contactList(request):
    if request.user.is_staff:
        contactMessageList = contactMessage.objects.all()
        paginator = Paginator(contactMessageList, 5)
        pageNum = request.GET.get('page')
        filteredMessageList = paginator.get_page(pageNum)   
        data = {
            'filteredMessageList':filteredMessageList,
        }
    else:
        return redirect('home:home')
    return render(request,"contactUs/contactList.html",data)

def contactUsDetail(request,id):
    if request.user.is_staff:
        try:
            contactUsMessage = contactMessage.objects.get(pk=id)
            data = {
                'contactUsMessage':contactUsMessage
            }
        except contactMessage.DoesNotExist:
            return redirect('contactUs:contactList')
    else:
        return redirect('home:home')
    return render(request,"contactUs/contactDetail.html",data)