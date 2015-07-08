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
    url(r'^nfceast.html$', views.nfceast),
    url(r'^nfcsouth.html$', views.nfcsouth),
    
    url(r'^dallascowboys.html$', views.dallascowboys),
    url(r'^houstontexans.html$', views.houstontexans),
    url(r'^tbbuccaneers.html$', views.tbbuccaneers),

    url(r'^DuaneBrown.html$', views.duanebrown),
    url(r'^LarryEnglish.html$', views.larryenglish),
    url(r'^TonyRomo.html$', views.tonyromo),

    url(r'^divisions.html$', views.divisions),
    url(r'^teams.html$', views.teams),
    url(r'^players.html$', views.players),
]