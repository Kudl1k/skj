from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from .models import League, Category, Match, Team, Player, PlayerHistory, EditHistory
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.

def home(request, league_id=None, match_id=None):
    match = None
    match_history = None
    category = Category.objects.get(name='Football')
    leagues = League.objects.filter(id_category=category)
    if league_id:
        league = League.objects.get(id=league_id)
        if match_id:
            match = Match.objects.get(id=match_id)
            match_history = EditHistory.objects.filter(id_match=match_id)
        else:
            match = None
        matches = Match.objects.filter(id_league=league)
    else:
        matches = None

    context = {
        'leagues': leagues,
        'matches': matches,
        'selected_match': match,
        'match_history': match_history,
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

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'base/login.html', {'form': form})

def user_logout(request):
    auth_logout(request)
    return redirect('login')


def user_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully')
        else:
            return HttpResponse(f'Form is not valid: {form.errors}')
    else:
        form = UserRegistrationForm()

    context = { 'form': form }
    return render(request, 'base/signup.html', context)

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

def players_hockey(request, league_id=None, team_id=None, player_id = None):
    category = Category.objects.get(name='Ice Hockey')
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
        'title': 'Ice Hockey Players',
        'type_view': 'players'
    }
    return render(request, 'base/players.html', context)

def players_basketball(request, league_id=None, team_id=None, player_id = None):
    category = Category.objects.get(name='Basketball')
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
        'title': 'Basketball Players',
        'type_view': 'players'
    }
    return render(request, 'base/players.html', context)