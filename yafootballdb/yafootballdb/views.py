from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from yafbdb.models import *

#def home(request):
#    template = loader.get_template('home.html')
#    return HttpResponse(template.render())

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)

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

def division(request, d_name):
    context = RequestContext(request)
    div = Division.objects.get(division=d_name.replace("_"," "))
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
        'team0url' : teams[0].team.replace(" ", "_").lower(),
        'team1' : teams[1].team,
        'team1url' : teams[1].team.replace(" ", "_").lower(),
        'team2' : teams[2].team,
        'team2url' : teams[2].team.replace(" ", "_").lower(),
        'team3' : teams[3].team,
        'team3url' : teams[3].team.replace(" ", "_").lower(),
    }
    return render_to_response('division_template.html', context_dict, context)

def team(request, t_name):
    context = RequestContext(request)
    tea = Team.objects.get(team=t_name.replace("_"," "))
    players = Player.objects.all().filter(team=tea)
    player_names = sorted([x.name for x in players])
    p = zip(player_names,['../players/' + x.replace(" ","_") for x in player_names])
    context_dict = {    
        'team' : tea.team,
        'division' : tea.division.division,
        'division_url' : '../divisions/' + tea.division.division.replace(" ","_"),
        'timage' : '../' + tea.timage,
        'state' : tea.state,
        'city' : tea.city,
        'stadium' : tea.stadium,
        'simage' : tea.simage,
        'coach' : tea.coach,
        'established' : tea.established,
        'cchamps' : tea.cchamps,
        'schamps' : tea.schamps,
        'pinfo' : p,

    }
    return render_to_response('team_template.html', context_dict, context)

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
