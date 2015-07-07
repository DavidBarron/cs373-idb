from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^home.html$', views.home),
    url(r'^about.html$', views.about),

    url(r'^afceast.html$', views.afceast),
    url(r'^afcsouth.html$', views.afcsouth),
    
    
    url(r'^dallascowboys.html$', views.dallascowboys),

    url(r'^divisions.html$', views.divisions),
    url(r'^teams.html$', views.teams),
    url(r'^players.html$', views.players),
]