from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import contactMessage, MessageReadByUser, ContactMessageReplies, ContactMessageToken
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from contactUs.random import RandomStringGenerator
from django.core.mail import send_mail
from djangoPractice.keys import *
from datetime import timedelta, datetime
from django.utils import timezone

# Create your views here.


def contactUs(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
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
                # contact message başarılı bi şekilde kaydedildi, şimdi token oluşturup mail gönderebiliriz.
                body = f"Hello {name}\nYour message has been received!\nIf you wish to add anyhing to your contact message, you can reply via below url:"
                mailList = list(email)
                #send_mail(subject, body, EMAIL_HOST_USER, mailList)
                
                flag=True
                while(flag):
                    token = RandomStringGenerator(20)
                    try:
                        xyz = ContactMessageToken.objects.get(token=token)
                    except ContactMessageToken.DoesNotExist:
                        flag=False

                daysKeep = 30
                expryDateAfterDayskeep = datetime.now() + timedelta(days = daysKeep)
                tokenObject = ContactMessageToken(messageId=a ,token=token ,expiryDate=expryDateAfterDayskeep)
                tokenObject.save()
            except contactMessage.DoesNotExist:
                messages.error(request, 'Invalid entry')
        else:
            messages.error(request, "Invalid Entry")
    return render(request,"contactUs/contact.html")



def contactList(request):
    if request.user.is_staff:
        contactMessageList = contactMessage.objects.all()
        messagesMyUserSaw = MessageReadByUser.objects.filter(read_userId=request.user.id)
        listOfMessages = [item.messageId for item in messagesMyUserSaw]
        paginator = Paginator(contactMessageList, 5)
        pageNum = request.GET.get('page')
        filteredMessageList = paginator.get_page(pageNum)   
        data = {
            'filteredMessageList':filteredMessageList,
            'listOfMessages':listOfMessages,
        }
    else:
        return redirect('home:home')
    return render(request,"contactUs/contactList.html",data)


def contactUsDetail(request,id):
    if request.user.is_staff:
        try:
            contactUsMessage = contactMessage.objects.get(pk=id)
            try:
                a = MessageReadByUser.objects.get(messageId=id, read_userId=request.user.id)
            except MessageReadByUser.DoesNotExist:
                a = MessageReadByUser(messageId=contactUsMessage, read_userId=request.user)
                a.save()
        except contactMessage.DoesNotExist:
            return redirect('contactUs:contactList')
        if request.method=='POST':
            newMessage = request.POST.get('reply')
            contactUsMessage = contactMessage.objects.get(pk=id)
            b = ContactMessageReplies(contactMessageId=contactUsMessage,isClient=False,replyUserId=request.user,replyMessage=newMessage)
            b.save()
        readByUserList = MessageReadByUser.objects.filter(messageId=id)
        replyMessages = ContactMessageReplies.objects.filter(contactMessageId=id)
        data = {
                'contactUsMessage':contactUsMessage,
                'readByUserList':readByUserList,
                'replyMessages':replyMessages,
            }   
    else:
        return redirect('home:home')
    return render(request,"contactUs/contactDetail.html",data)


def contactUsReply(request,msgId,token):
    isClientView = True
    try:
        verify = ContactMessageToken.objects.get(messageId=msgId,token=token)
        if verify.expiryDate > timezone.now():
            print("timezonenow: ",timezone.now(), "expiryDate: ",verify.expiryDate, "\n\n\n")
            contactUsMessage = contactMessage.objects.get(pk=msgId)
            replyMessages = ContactMessageReplies.objects.filter(contactMessageId=msgId)
        else:
            messages.error(request, 'Expired Token!')
            return redirect('home:home')
    except ContactMessageToken.DoesNotExist:
        messages.error(request, 'Token & Id do not match!')
        return redirect('home:home')
    data = {
        'contactUsMessage':contactUsMessage,
        'isClientView':isClientView,
        'replyMessages':replyMessages,
        }
    return render(request,"contactUs/contactDetail.html",data)