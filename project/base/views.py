from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .models import League, Category, Match, Team, Player, PlayerHistory

# Create your views here.

def home(request, league_id=None, match_id=None):
    match = None
    category = Category.objects.get(name='Football')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        league = League.objects.get(id=league_id)
        if match_id:
            match = Match.objects.get(id=match_id)
        else:
            match = None
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'selected_match': match,
        'title': 'Football Results',
        'type_view': 'results',
    }
    return render(request, 'base/home.html', context)

def hockey(request, league_id=None,match_id= None):
    match = None
    category = Category.objects.get(name='Ice Hockey')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        league = League.objects.get(id=league_id)
        if match_id:
            match = Match.objects.get(id=match_id)
        else:
            match = None
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'selected_match': match,
        'title': 'Ice Hockey Results',
        'type_view': 'results',
    }
    return render(request, 'base/home.html', context)

def basketball(request, league_id=None,match_id= None):
    match = None
    category = Category.objects.get(name='Basketball')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        league = League.objects.get(id=league_id)
        if match_id:
            match = Match.objects.get(id=match_id)
        else:
            match = None
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'selected_match': match,
        'title': 'Basketball Results',
        'type_view': 'results',
    }
    return render(request, 'base/home.html', context)

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/singup.html')

def players_football(request, league_id=None, team_id=None, player_id = None):
    category = Category.objects.get(name='Football')
    leagues = League.objects.filter(id_category=category)
    teams = None
    players = None
    player_info = None
    if league_id:
        teams = Team.objects.filter(id_league=league_id)
        if team_id:
            player_histories = PlayerHistory.objects.filter(Q(id_team=team_id) & (Q(end_date__isnull=True) | Q(end_date__gte=timezone.now())))
            players = [{'player': history.id_player, 'history': history} for history in player_histories]
            if player_id:
                player = Player.objects.get(id=player_id)
                player_history = PlayerHistory.objects.filter(id_player=player_id)
                player_info = {'player': player, 'history': player_history}
    context = {
        'leagues': leagues,
        'teams': teams,
        'players': players,
        'player_info': player_info,
        'title': 'Football Players',
        'type_view': 'players'
    }
    return render(request, 'base/players.html', context)