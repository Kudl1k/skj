from django.shortcuts import render
from .models import League, Category, Match

# Create your views here.

rooms = [
    {'id': 1, 'name' : 'Room 1'},
    {'id': 2, 'name' : 'Room 2'},
    {'id': 3, 'name' : 'Room 3'}
]

def home(request):
    category = Category.objects.get(name='Football')
    leagues = League.objects.filter(id_category=category)
    matches = Match.objects.filter(id_category=category)
    context = {
        'leagues': leagues,
        'matches': matches,
        'title': 'Football Page',
    }
    return render(request, 'base/home.html', context)

def hockey(request):
    category = Category.objects.get(name='Ice Hockey')
    leagues = League.objects.filter(id_category=category)
    print(leagues)
    context = {
        'leagues': leagues,
        'title': 'Ice hockey Page',
    }
    return render(request, 'base/home.html', context)

def basketball(request):
    category = Category.objects.get(name='Basketball')
    leagues = League.objects.filter(id_category=category)
    print(leagues)
    context = {
        'leagues': leagues,
        'title': 'Basketball Page',
    }
    return render(request, 'base/home.html', context)

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/singup.html')