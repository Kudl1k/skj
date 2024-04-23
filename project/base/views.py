from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import League, Category, Match

# Create your views here.

rooms = [
    {'id': 1, 'name' : 'Room 1'},
    {'id': 2, 'name' : 'Room 2'},
    {'id': 3, 'name' : 'Room 3'}
]

def home(request, league_id=None,match_id= None):
    category = Category.objects.get(name='Football')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        print(league_id)
        if match_id:
            league = League.objects.get(name=league_id)
        else:
            league = League.objects.get(id=league_id)
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    if match_id:
        selected_match = get_object_or_404(Match, id=match_id)
    else:
        selected_match = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'selected_match': selected_match,
        'title': 'Football Page',
    }
    return render(request, 'base/home.html', context)

def hockey(request, league_id=None,match_id= None):
    category = Category.objects.get(name='Ice Hockey')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        league = League.objects.get(id=league_id)
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'title': 'Football Page',
    }
    return render(request, 'base/home.html', context)

def basketball(request, league_id=None,match_id= None):
    category = Category.objects.get(name='Basketball')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        league = League.objects.get(id=league_id)
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'title': 'Football Page',
    }
    return render(request, 'base/home.html', context)

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/singup.html')