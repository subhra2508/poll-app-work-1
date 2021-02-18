from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from polls.models import Post
from .forms import profileUpdateForm
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
@login_required
def profileView(request):
    profile=request.user.profile
    form=profileUpdateForm(instance=profile)
    if request.method=="POST":
        form=profileUpdateForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render(request,'profiles/settings.html',context)
@login_required
def dashboardView(request):
    posts=Post.objects.filter(author=request.user.profile)
    context={"posts":posts}
    return render(request,'profiles/dashboard.html',context)
@login_required
def chartDataView(request):
    context={}
    return render(request,"profiles/charts.html",context)
class ChartData(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self,request,format=None):
        labels=["Movies","Sports","Political","General"]
        default_items=[23, 2, 3, 12]
        data={
            "labels":labels,
            "default":default_items
        }
        return Response(data)