from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404


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

def afcsouth(request):
    template = loader.get_template('afcsouth.html')
    return HttpResponse(template.render())

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
    template = loader.get_template('duanebrown.html')
    return HttpResponse(template.render())

def larryenglish(request):
    template = loader.get_template('larryenglish.html')
    return HttpResponse(template.render())

def tbbuccaneers(request):
    template = loader.get_template('tbbuccaneers.html')
    return HttpResponse(template.render())

def tonyromo(request):
    template = loader.get_template('tonyromo.html')
    return HttpResponse(template.render())
