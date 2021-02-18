from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import createNewPostForm,giveCommentForm
from django.contrib.auth.models import User
from .models import Post,Comment
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def homeView(request):
    post=Post.objects.all()
    lst={}
    lst1=[]
    for i in post:
        lst[i.like.count()]=i
    for j in sorted(lst):
        lst1.append(lst[j])
    lst1.reverse()
    form=giveCommentForm(request.POST or None)
    context={"post":post,"lst1":lst1,"form":form}
    return render(request,'polls/home.html',context);
@login_required
def commentView(request,id):
    post=Post.objects.get(id=id)
    form=giveCommentForm(request.POST or None)
    comments=Comment.objects.all()
    if request.method=="POST":
        form=giveCommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user.profile
            instance.post=Post.objects.get(id=id)
            instance.save()
            return redirect('/')
        else:
            return HttpResponse("Plz enter a valid Form!")
    context={"form":form,"post":post,'comments':comments}
    return render(request,'polls/comment.html',context)
@login_required
def likeView(request,id):
    currentUser=request.user
    print(request.user)
    currPost=Post.objects.get(id=id)
    print(currPost,id)

    if currPost.like.all() or currPost.dislike.all():
        for i in currPost.like.all():
            if currentUser == i:
                currPost.like.remove(currentUser)
                break
            else:
                for i in currPost.dislike.all():
                    if i == currentUser:
                        currPost.dislike.remove(currentUser)
                        break
                    else:
                        currPost.like.add(currentUser)
    else:
        currPost.like.add(currentUser)
    return redirect('/')
@login_required
def unLikeView(request,id):
    currentUser=request.user
    currentPost=Post.objects.get(id=id)
    if currentPost.dislike.all() or currentPost.like.all():
        for i in currentPost.dislike.all():
            if currentUser==i:
                currentPost.dislike.remove(currentUser)
                break
            else:
                for i in currentPost.like.all():
                    if i == currentUser:
                        currentPost.like.remove(currentUser)
                        break
                    else:
                        currentPost.dislike.add(currentUser)
    else:
        currentPost.dislike.add(currentUser)
    return redirect('/')
@login_required
def createNewPostView(request):
    form=createNewPostForm(request.POST or None)
    if request.method=="POST":
        form=createNewPostForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user.profile
            instance.save()
            return redirect('home')
    context={"form":form}
    return render(request,'polls/createpost.html',context)

