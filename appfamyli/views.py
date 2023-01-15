from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .models import *


# Create your views here.

def index(request):
    one_form = MyForm()
    return render(request, 'index.html', {'form': one_form})
        # HttpResponse('<h1>Главная страница, сформированная через представление</h1>')

def team(request, town_id):
    teams = Team.objects.filter(parent=town_id)
    team_list = []
    for team_el in teams:
        team_list.append({'id': team_el.id, 'name': team_el.name})
    return JsonResponse(team_list, safe=False)

def subteam(request, team_id):
    subteams = SubTeam.objects.filter(parent=team_id)
    subteam_list = []
    for subteam_el in subteams:
        subteam_list.append({'id': subteam_el.id, 'name': subteam_el.name})
    return JsonResponse(subteam_list, safe=False)

def view_in_browser(request, parent_id):
    return HttpResponse(parent_id)


def item1(request):
    return render(request, 'item1.html')
    # return HttpResponse('<h1>Пункт 1</h1>')

def item2(request):
    return HttpResponse('<h1>Пункт 2</h1>')

def item3(request):
    return HttpResponse('<h1>Пункт 3</h1>')