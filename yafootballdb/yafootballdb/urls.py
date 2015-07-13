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


    url(r'^divisions/afceast$', views.afceast),
    url(r'^divisions/afcsouth$', views.division, kwargs={'d_name':'AFC South'}),
    url(r'^divisions/nfceast$', views.nfceast),
    url(r'^divisions/nfcsouth$', views.nfcsouth),
    
    url(r'^teams/dallascowboys$', views.dallascowboys),
    url(r'^teams/houstontexans$', views.houstontexans),
    url(r'^teams/tbbuccaneers$', views.tbbuccaneers),

    url(r'^players/DuaneBrown$', views.duanebrown),
    url(r'^players/LarryEnglish$', views.larryenglish),
    url(r'^players/TonyRomo$', views.tonyromo),

    url(r'^divisions/$', views.divisions),
    url(r'^teams/$', views.teams),
    url(r'^players/$', views.players),
]
