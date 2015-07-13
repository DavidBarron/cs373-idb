from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from yafbdb.models import *

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def divisions(request):
    template = loader.get_template('divisions.html')
    return HttpResponse(template.render())

def teams(request):
    template = loader.get_template('teams.html')
    return HttpResponse(template.render())

def players(request):
    template = loader.get_template('players.html')
    return HttpResponse(template.render())


def afceast(request):
    template = loader.get_template('afceast.html')
    return HttpResponse(template.render())

def division(request, d_name):
    context = RequestContext(request)
    div = Division.objects.get(division=d_name)
    teams = list(Team.objects.all().filter(division=div))
    context_dict = {
        'division' : div.division,
        'dimage' : div.dimage,
        'conference' : div.conference,
        'cimage' : div.cimage,
        'founded' : div.founded,
        'rchamp' : div.rchamp,
        'mchamps' : div.mchamps,
        'cnum' : div.cnum,
        'team0' : teams[0].team,
        'team0url' : teams[0].team.replace(" ", "").lower() + ".html",
        'team1' : teams[1].team,
        'team1url' : teams[1].team.replace(" ", "").lower() + ".html",
        'team2' : teams[2].team,
        'team2url' : teams[2].team.replace(" ", "").lower() + ".html",
        'team3' : teams[3].team,
        'team3url' : teams[3].team.replace(" ", "").lower() + ".html",
    }
    return render_to_response('division_template.html', context_dict, context)

#def afcsouth(request):
#    template = loader.get_template('afcsouth.html')
#    return HttpResponse(template.render())

def nfceast(request):
    template = loader.get_template('nfceast.html')
    return HttpResponse(template.render())


def nfcsouth(request):
    template = loader.get_template('nfcsouth.html')
    return HttpResponse(template.render())

def dallascowboys(request):
    template = loader.get_template('dallascowboys.html')
    return HttpResponse(template.render())

def houstontexans(request):
    template = loader.get_template('houstontexans.html')
    return HttpResponse(template.render())

def tbbuccaneers(request):
    template = loader.get_template('tbbuccaneers.html')
    return HttpResponse(template.render())

def duanebrown(request):
    template = loader.get_template('DuaneBrown.html')
    return HttpResponse(template.render())

def larryenglish(request):
    template = loader.get_template('LarryEnglish.html')
    return HttpResponse(template.render())

def tbbuccaneers(request):
    template = loader.get_template('tbbuccaneers.html')
    return HttpResponse(template.render())

def tonyromo(request):
    template = loader.get_template('TonyRomo.html')
    return HttpResponse(template.render())
