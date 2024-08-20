from django.shortcuts import render, redirect
import requests
from .models import UserCity
from django.urls import reverse

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        cityList = UserCity.objects.filter(user=request.user)
        cityData = []
        for city in cityList:
            a = city.city.name
            url = "http://api.weatherapi.com/v1/current.json?key=f694b0491b6e4fd5b73200913240808&q=" + a
            response =requests.get(url)
            if response.status_code==200:
                jsonData = response.json()
                temperature = jsonData['current']['temp_c']
                currentSky = jsonData['current']['condition']['text']
                imageUrl = jsonData['current']['condition']['icon'][2:]
                cityData.append({'name':a,'temperature':temperature,'currentSky':currentSky, 'imageUrl':imageUrl })
            else:
                cityData.append({'name':a, 'isError':True })
    else:
        loginUrl = reverse("user:userLogin")
        nextUrl = reverse("weather:home")
        url = loginUrl+"?next="+nextUrl
        return redirect(url)
    data = {
        'cities':cityData
    }
    return render(request,'weather/index.html',data)