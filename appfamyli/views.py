from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .models import Child


# Create your views here.

def index(request):
    one_form = MyForm()
    return render(request, 'index.html', {'form': one_form})
        # HttpResponse('<h1>Главная страница, сформированная через представление</h1>')

def children(request, parent_id):
    children = Child.objects.filter(parent=parent_id)
    children_list = []
    for child in children:
        children_list.append({'id': child.id, 'name': child.name})
    return JsonResponse(children_list, safe=False)

def view_in_browser(request, parent_id):
    return HttpResponse(parent_id)
