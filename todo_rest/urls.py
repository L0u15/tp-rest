"""todo_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from todo import views

urlpatterns = format_suffix_patterns([
    path('admin/',
         admin.site.urls),
    path('',
         views.api_root),
    path('todos/',
         views.TodoList.as_view(),
         name='todo-list'),
    path('todo/<int:pk>/',
         views.TodoDetail.as_view(),
         name='todo-detail'),
     path('users/',
          views.UserList.as_view(),
          name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
])

#urlpatterns = format_suffix_patterns(urlpatterns)
