from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import League, Category, Match, Team, Player, PlayerHistory, EditHistory, Favourite
from .forms import UserLoginForm, UserRegistrationForm, EditMatchForm, AddMatchHistoryForm

# Create your views here.

def home(request, league_id=None, match_id=None):
    match = None
    match_history = None
    league = None
    category = Category.objects.get(name='Football')
    leagues = League.objects.filter(id_category=category)
    favourites = []
    if request.user.is_authenticated:
        favourites = Favourite.objects.filter(user=request.user).values_list('id_match_id', flat=True)
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
        'selected_league': league,
        'selected_category': category,
        'match_history': match_history,
        'favourites': favourites,
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

    context = { 
        'form': form,
        'title': "Log in"
    }
    return render(request, 'base/login.html', context)

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

    context = { 
        'form': form,
        'title': "Sign in"
    }
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

@login_required
def favourite_match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    favourite, created = Favourite.objects.get_or_create(user=request.user, id_match=match)
    if not created:
        favourite.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def edit_match(request, match_id):
    match = Match.objects.get(id=match_id)
    match_history = EditHistory.objects.filter(id_match=match_id)
    form1 = EditMatchForm(instance=match)
    form2 = AddMatchHistoryForm()

    if request.method == 'POST':
        print(request.POST)
        if 'form1' in request.POST:
            date_string = request.POST['start_time_date']
            time_string = request.POST['start_time_time']
            match.start_time = timezone.make_aware(datetime.strptime(f"{date_string} {time_string}", "%Y-%m-%d %H:%M"))
            match.viewers = request.POST['viewers']
            match.stadium = request.POST['stadium']
            match.save()  # Save the match instance after updating start_time
        elif 'form2' in request.POST:
            new_history = EditHistory()
            new_history.id_match = match
            new_history.user = request.user
            new_history.old_score1 = match.score_1
            new_history.old_score2 = match.score_2
            new_history.new_score1 = request.POST['new_score1']
            new_history.new_score2 = request.POST['new_score2']
            match.score_1 = new_history.new_score1
            match.score_2 = new_history.new_score2
            new_history.modified_at = timezone.now()
            new_history.save()
            match.save()
    context = {
        'title': 'Edit Match',
        'match': match,
        'match_history': match_history,
        'form1': form1,
        'form2': form2
    }
    return render(request,'base/edit_match.html',context)

def delete_match(request, match_id):
    match = Match.objects.get(id=match_id)
    match.delete()
    football_category = Category.objects.get(name='Football')
    basketball_category = Category.objects.get(name='Basketball')
    hockey_category = Category.objects.get(name='Ice Hockey')
    if match.id_category == football_category:
        return redirect('/football/results')
    if match.id_category == basketball_category:
        return redirect('/basketball/results')
    if match.id_category == hockey_category:
        return redirect('/hockey/results')
    return redirect('/football/results')

@login_required
def create_match(request,category_id,league_id):
    teams = Team.objects.filter(id_league=league_id)
    category = Category.objects.get(id=category_id)
    league = League.objects.get(id=league_id)

    context = {
        'selected_category': category_id,
        'selected_league': league_id,
        'teams': teams
    }
    if request.method == 'POST':
        if 'form1' in request.POST:
            match = Match()
            date_string = request.POST['start_time_date']
            time_string = request.POST['start_time_time']
            team_1 = Team.objects.get(id=request.POST['id_team_1'])
            team_2 = Team.objects.get(id=request.POST['id_team_2'])
            match.score_1 = 0
            match.score_2 = 0
            match.start_time = timezone.make_aware(datetime.strptime(f"{date_string} {time_string}", "%Y-%m-%d %H:%M"))
            match.end_time = match.start_time + timedelta(hours=1.5)
            match.viewers = request.POST['viewers']
            match.stadium = request.POST['stadium']
            match.id_category = category
            match.id_league = league
            match.user = request.user
            match.id_team_1 = team_1
            match.id_team_2 = team_2
            match.save()
            football_category = Category.objects.get(name='Football')
            basketball_category = Category.objects.get(name='Basketball')
            hockey_category = Category.objects.get(name='Ice Hockey')
            if category == football_category:
                return redirect('/football/results')
            if category == basketball_category:
                return redirect('/basketball/results')
            if category == hockey_category:
                return redirect('/hockey/results')    
    return render(request,'base/create_match.html',context)