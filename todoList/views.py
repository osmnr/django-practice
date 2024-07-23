from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Todolist
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
# Create your views here.

def todoList(request):
    if request.method == 'POST':
        newTask = request.POST.get('taskSubject')
        if len(newTask)<=3:
            messages.error(request, 'The task should have at least 4 characters.')
        else:
            a = Todolist(taskName=newTask) 
            a.save()
    pageFilter = request.GET.get('filter')
    if pageFilter:
        if pageFilter.lower() == 'undone':
            taskList = Todolist.objects.filter(isDeleted=False, isDone=False).order_by('updatedDate','id')
        elif pageFilter.lower() == 'done':
            taskList = Todolist.objects.filter(isDeleted=False, isDone=True).order_by('updatedDate','id')
        elif pageFilter.lower() == 'deleted':
            taskList = Todolist.objects.filter(isDeleted=True).order_by('updatedDate','id')
        else:
            return redirect('todoList:index')
    else:
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
    }
    return render(request, 'todoList/todoList.html',data)

def updateTodoItem(request, pk):
    try:
        todoItem = Todolist.objects.get(pk=pk)
        if todoItem.isDone:
            todoItem.isDone = False
        else:
            todoItem.isDone = True
        todoItem.save()
        return redirect('todoList:index')
    except Todolist.DoesNotExist:
        return redirect('todoList:index')
    

def deletedTodoItem(request, xxx):
    try:
        todoItem = Todolist.objects.get(pk=xxx)
        todoItem.isDeleted = True
        todoItem.save()
        return redirect('todoList:index')
    except Todolist.DoesNotExist:
        return redirect('todoList:index')
    
