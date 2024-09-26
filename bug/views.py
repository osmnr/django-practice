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
    #filtering the comment list depending on the user's staff auth
    if not request.user.is_staff:
        commentList = Comment.objects.filter(source=bug.id, isDevNote=False).order_by('date','id')
    # adding new comment to db
    if request.method=='POST':
        newComment = request.POST.get('comment')
        isDev = request.user.is_staff
        a = Comment(source=bug, commenter=request.user, comment=newComment, isDevNote=isDev)
        a.save()
    data = {
        'bug':bug,
        'commentList': commentList,
    }
    return render(request, 'bug/detail.html', data)