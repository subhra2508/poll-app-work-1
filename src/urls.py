"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from polls.views import (
    homeView,
    likeView,
    unLikeView,
    createNewPostView,
    commentView,
)
from profiles.views import(
    profileView,
    dashboardView,
    ChartData,
    chartDataView,
   
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='home'),
    path('like/<int:id>/',likeView,name='like-post'),
    path('unlike/<int:id>/',unLikeView,name='unlike-post'),
    path('comment/<int:id>/',commentView,name='blog-comment'),
    path('settings/',profileView,name="settings"),
    path('profile/dashboard/',dashboardView,name="dashboard"),
    path('create/',createNewPostView,name="create-newpost"),
    path('api/chart/data/',ChartData.as_view(),name="api-data"),
    path('chart/view/',chartDataView),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
