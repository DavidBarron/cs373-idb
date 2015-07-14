"""yafootballdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', views.home),
    url(r'^about$', views.about),
    url(r'^$', views.home),

    #this is the parent divisions url
    url(r'^divisions/$', views.divisions),
    #this one is a for a specfic division
    url(r'^divisions/(?P<d_name>\w+)/$', views.division), 
    
   #this is the parent teams url
    url(r'^teams/$', views.teams),
    #this one is a for a specfic team
    url(r'^teams/(?P<t_name>\w+)/$', views.team), 

   #this is the parent players url
    url(r'^players/$', views.players),
    #this one is a for a specfic player
    url(r'^players/(?P<p_name>\w+)/$', views.player), 
]
