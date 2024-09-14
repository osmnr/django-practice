from django.shortcuts import render
from .models import Bug, Comment
# Create your views here.

def bug(request):
    buglist = Bug.objects.all()
    data = {
        'buglist':buglist
    }
    return render(request, 'bug/index.html',data)



def detail(request, id):
    bug = Bug.objects.get(id=id)
    commentList = Comment.objects.filter(source=bug.id).order_by('date','id')
    data = {
        'bug':bug,
        'commentList': commentList,
    }
    return render(request, 'bug/detail.html', data)