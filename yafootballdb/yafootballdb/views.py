from django.shortcuts import render
from rest_framework import viewsets
from yafbdb.serializers import *
import os

from json import dumps, loads
try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from yafbdb.models import *
from time import sleep
import random

#def home(request):
#    template = loader.get_template('home.html')
#    return HttpResponse(template.render())

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def tests(request):
    context = RequestContext(request)
    os.system("python3 manage.py test > myTest.out 2>&1")
    sleep(1)
    testFile = open("myTest.out")
    s = testFile.read()
    testFile.close()
    context_dict = { "results" : s }
    return render_to_response('tests.html', context_dict, context)

def divisions(request):
    try:
        context = RequestContext(request)
        divs = Division.objects.all()
        context_tup = tuple()
        for div in divs :
            context_tup += ((div.division,
                            '/divisions/' + div.division.replace(" ","_"),
                            div.conference,
                            div.founded,
                            div.rchamp,
                            '../teams/' + div.rchamp.replace(" ","_"),
                            div.mchamps,
                            '../teams/' + div.mchamps.replace(" ","_"),
                            div.cnum),)
        context_dict = {
            'dinfo' : context_tup
        }
        return render_to_response('divisions.html', context_dict, context)
    except:
        return handler404(request)

def teams(request):
    try:
        context = RequestContext(request)
        teas = Team.objects.all()
        context_tup = tuple()
        for tea in teas :
            context_tup += ((tea.team,
                            '../teams/' + tea.team.replace(" ","_"),
                            tea.division.division,
                            '../divisions/' + tea.division.division.replace(" ","_"),
                            tea.city,
                            tea.state,
                            tea.stadium,
                            tea.coach,
                            tea.established),)
        context_dict = {
            'tinfo' : context_tup
        }
        return render_to_response('teams.html', context_dict, context)
    except:
        return handler404(request)

def players(request):
    try:
        context = RequestContext(request)
        plas = Player.objects.all()
        context_tup = tuple()
        for pla in plas :
            context_tup += ((pla.name,
                            '/players/' + pla.name.replace(" ","_"),
                            pla.number,
                            pla.team.team,
                            '../teams/' + pla.team.team.replace(" ","_"),
                            pla.position,
                            pla.college,
                            pla.height,
                            pla.weight,
                            pla.experience),)
        context_dict = {
            'pinfo' : context_tup
        }
        return render_to_response('players.html', context_dict, context)
    except:
        return handler404(request)

def other_api(request):
    # try:
        context = RequestContext(request)

        url =  "http://8bytedining.me/"
        request = Request(url+"api/recipes")    
        response = urlopen(request)
        response_body = response.read().decode("utf-8") 
        response_data = loads(response_body)

        context_tup = tuple()
        # for recipe in response_data:
        #     context_tup += ((
        #                     recipe["name"],
        #                     recipe["img"],
        #                     "http://8bytedining.me/recipes" + recipe["recipe_id"]
        #                     ),)

        #Pick random numbers of index
        for x in range(5):
            recipe = response_data[random.randint(0, 499)] 
            context_tup += ((
                            recipe["name"],
                            recipe["img"],
                            "http://8bytedining.me/recipes/" + recipe["recipe_id"]
                            ),) 
        context_dict = {'recipe_info' : context_tup}
        return render_to_response('other_api_page.html', context_dict, context)
    # except:
        # return handler404(request)

def division(request, d_name):
    try:
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
            'team0url' : '../../teams/' + teams[0].team.replace(" ", "_"),
            'team1' : teams[1].team,
            'team1url' : '../../teams/' + teams[1].team.replace(" ", "_"),
            'team2' : teams[2].team,
            'team2url' : '../../teams/' + teams[2].team.replace(" ", "_"),
            'team3' : teams[3].team,
            'team3url' : '../../teams/' + teams[3].team.replace(" ", "_"),
        }
        return render_to_response('division_template.html', context_dict, context)
    except:
        return handler404(request)


def team(request, t_name):
    try:
        context = RequestContext(request)
        tea = Team.objects.get(team=t_name.replace("_"," "))
        players = Player.objects.all().filter(team=tea)
        player_names = sorted([x.name for x in players])
        p = zip(player_names,['../../players/' + x.replace(" ","_") for x in player_names])
        context_dict = {    
            'team' : tea.team,
            'division' : tea.division.division,
            'division_url' : '../../divisions/' + tea.division.division.replace(" ","_"),
            'timage' : '/' + tea.timage,
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
    except:
        return handler404(request)

def player(request, p_name):
    try:
        context = RequestContext(request)
        pla = Player.objects.get(name=p_name.replace("_"," "))
        context_dict = {    
            'name' : pla.name,
            'team' : pla.team,
            'team_url' : '../../teams/' + pla.team.team.replace(" ","_"),
            'number' : pla.number,
            'position' : pla.position,
            'height' : pla.height,
            'weight' : pla.weight,
            'age' : pla.age,
            'experience' : pla.experience,
            'college' : pla.college,
            'pimage' : pla.pimage,
        }
        return render_to_response('player_template.html', context_dict, context)
    except:
        return handler404(request)


#Error 404 page
def handler404(request):
    return render(request, '404page.html')

class DivisionViewSet(viewsets.ModelViewSet) :
    """
    """
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class TeamViewSet(viewsets.ModelViewSet) :
    """
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet) :
    """
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer