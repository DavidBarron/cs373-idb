from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def home(request):
    template = loader.get_template('polls/home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('polls/about.html')
    return HttpResponse(template.render())


def divisions(request):
    template = loader.get_template('polls/divisions.html')
    return HttpResponse(template.render())

def teams(request):
    template = loader.get_template('polls/teams.html')
    return HttpResponse(template.render())

def players(request):
    template = loader.get_template('polls/players.html')
    return HttpResponse(template.render())


def afceast(request):
    template = loader.get_template('polls/afceast.html')
    return HttpResponse(template.render())

def afcsouth(request):
    template = loader.get_template('polls/afcsouth.html')
    return HttpResponse(template.render())

def nfceast(request):
    template = loader.get_template('polls/nfceast.html')
    return HttpResponse(template.render())

def nfcsouth(request):
    template = loader.get_template('polls/nfcsouth.html')
    return HttpResponse(template.render())

def dallascowboys(request):
    template = loader.get_template('polls/dallascowboys.html')
    return HttpResponse(template.render())

def houstontexans(request):
    template = loader.get_template('polls/houstontexans.html')
    return HttpResponse(template.render())

def tbbuccaneers(request):
    template = loader.get_template('polls/tbbuccaneers.html')
    return HttpResponse(template.render())

def duanebrown(request):
    template = loader.get_template('polls/duanebrown.html')
    return HttpResponse(template.render())

def larryenglish(request):
    template = loader.get_template('polls/larryenglish.html')
    return HttpResponse(template.render())

def tbbuccaneers(request):
    template = loader.get_template('polls/tbbuccaneers.html')
    return HttpResponse(template.render())

def tonyromo(request):
    template = loader.get_template('polls/tonyromo.html')
    return HttpResponse(template.render())
