from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from todoList.models import UsersTodoList


# Create your views here.
def userLogin(request):
    previous_page = request.META.get('HTTP_REFERER')
    print("\n\n\n previouspage:", previous_page)
    if request.user.is_authenticated:
        return redirect('home:home')
    temp_session = request.session.session_key

    if request.method == 'POST':
        inputUserName = request.POST.get('username').lower()
        inputPassword = request.POST.get('password')
        user = authenticate(request, username=inputUserName, password=inputPassword)
        if user is not None:
            login(request,user)
            userLessTaskList = UsersTodoList.objects.filter(sessionKey=temp_session)
            for task in userLessTaskList:
                task.user=user
                task.save()
            if request.META.get('HTTP_REFERER'):
                print(request.META.get('HTTP_REFERER'),"\n\n")
                return redirect(request.META.get('HTTP_REFERER'))
            return redirect('home:home')
        else:
            print('username or password is incorrect')
    return render(request, 'user/userLogin.html')




def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        inputUserName = request.POST.get('username').lower()
        inputEmail = request.POST.get('email')
        inputPass = request.POST.get('password')
        inputPass2 = request.POST.get('password2')
        if inputPass == inputPass2:
            try:
                user = User.objects.create(username=inputUserName, password=inputPass, email=inputEmail)
                user.save()
                login(request, user)
                return redirect('home:home')
            except User.DoesNotExist:
                print('user register error')
        else:
            print('2 passwords are not same')
    return render(request, 'user/userRegister.html')





def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home:home')

