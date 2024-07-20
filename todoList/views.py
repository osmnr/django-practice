from django.shortcuts import render
from django.views.generic import ListView
from .models import Todolist
from datetime import datetime, timedelta
from django.utils import timezone


# Create your views here.

def todoList(request):
    taskList = Todolist.objects.filter(isDeleted=False).order_by('isDone','updatedDate','id')
    daysKeep = 3
    past_date_before_daysKeep = timezone.now() - timedelta(days = daysKeep)
    

    ## Todolist.objects.filter(updatedDate__lte=daysKeep) ## bunu kullanamadık.

    filteredList = [i for i in taskList if (i.isDone and i.updatedDate >= past_date_before_daysKeep) or not i.isDone ]
    
    # yukarıdaki tek satıra alternatif olarak:
    """ filteredList = []
    for i in taskList:
        if (i.isDone  and i.updatedDate >= past_date_before_daysKeep) or not i.isDone:
            filteredList.append(i)
         """


    data = {
        'filteredList':filteredList,
        'taskList':taskList,
        'past_date_before_daysKeep':past_date_before_daysKeep,
    }
    return render(request, 'todoList/todoList.html',data)