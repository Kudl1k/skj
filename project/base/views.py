from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date
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
    match_history = None
    league = None
    category = Category.objects.get(name='Ice Hockey')
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
        'title': 'Ice Hockey Results',
        'type_view': 'results',
    }
    return render(request, 'base/home.html', context)

def basketball(request, league_id=None,match_id= None):
    match = None
    match_history = None
    league = None
    category = Category.objects.get(name='Basketball')
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
    league = None
    teams = None
    team = None
    player = None
    players = None
    player_info = None
    if league_id:
        league = League.objects.get(id=league_id)
        teams = Team.objects.filter(id_league=league_id)
        if team_id:
            team = Team.objects.get(id=team_id)
            player_histories = PlayerHistory.objects.filter(Q(id_team=team_id) & (Q(end_date__isnull=True) | Q(end_date__gte=timezone.now())))
            players = [{'player': history.id_player, 'history': history} for history in player_histories]
            if player_id:
                player = Player.objects.get(id=player_id)
                player_history = PlayerHistory.objects.filter(id_player=player_id)
                player_info = {'player': player, 'history': player_history}
    context = {
        'selected_category': category,
        'leagues': leagues,
        'selected_league': league,
        'teams': teams,
        'selected_team': team,
        'players': players,
        'player_info': player_info,
        'selected_player': player,
        'title': 'Football Players',
        'type_view': 'players'
    }
    return render(request, 'base/players.html', context)

def players_hockey(request, league_id=None, team_id=None, player_id = None):
    category = Category.objects.get(name='Ice Hockey')
    leagues = League.objects.filter(id_category=category)
    league = None
    teams = None
    team = None
    player = None
    players = None
    player_info = None
    if league_id:
        league = League.objects.get(id=league_id)
        teams = Team.objects.filter(id_league=league_id)
        if team_id:
            team = Team.objects.get(id=team_id)
            player_histories = PlayerHistory.objects.filter(Q(id_team=team_id) & (Q(end_date__isnull=True) | Q(end_date__gte=timezone.now())))
            players = [{'player': history.id_player, 'history': history} for history in player_histories]
            if player_id:
                player = Player.objects.get(id=player_id)
                player_history = PlayerHistory.objects.filter(id_player=player_id)
                player_info = {'player': player, 'history': player_history}
    context = {
        'selected_category': category,
        'leagues': leagues,
        'selected_league': league,
        'teams': teams,
        'selected_team': team,
        'players': players,
        'player_info': player_info,
        'selected_player': player,
        'title': 'Ice Hockey Players',
        'type_view': 'players'
    }
    return render(request, 'base/players.html', context)

def players_basketball(request, league_id=None, team_id=None, player_id = None):
    category = Category.objects.get(name='Basketball')
    leagues = League.objects.filter(id_category=category)
    league = None
    teams = None
    team = None
    player = None
    players = None
    player_info = None
    if league_id:
        league = League.objects.get(id=league_id)
        teams = Team.objects.filter(id_league=league_id)
        if team_id:
            team = Team.objects.get(id=team_id)
            player_histories = PlayerHistory.objects.filter(Q(id_team=team_id) & (Q(end_date__isnull=True) | Q(end_date__gte=timezone.now())))
            players = [{'player': history.id_player, 'history': history} for history in player_histories]
            if player_id:
                player = Player.objects.get(id=player_id)
                player_history = PlayerHistory.objects.filter(id_player=player_id)
                player_info = {'player': player, 'history': player_history}
    context = {
        'selected_category': category,
        'leagues': leagues,
        'selected_league': league,
        'teams': teams,
        'selected_team': team,
        'players': players,
        'player_info': player_info,
        'selected_player': player,
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

@login_required
def create_league(request,category_id):
    context = {
        'title': 'Create League'
    }
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        if 'form1' in request.POST:
            league = League()
            league.name = request.POST['name']
            league.description = request.POST['description']
            league.id_category = category
            league.save();
            football_category = Category.objects.get(name='Football')
            basketball_category = Category.objects.get(name='Basketball')
            hockey_category = Category.objects.get(name='Ice Hockey')
            if category == football_category:
                return redirect('/football/players')
            if category == basketball_category:
                return redirect('/basketball/players')
            if category == hockey_category:
                return redirect('/hockey/players')  
    return render(request,'base/create_league.html',context)

def create_team(request, category_id, league_id):
    context = {
        'title': 'Create Team'
    }
    category = Category.objects.get(id=category_id)
    league = League.objects.get(id=league_id)
    if request.method == 'POST':
        if 'form1' in request.POST:
            team = Team()
            team.name = request.POST['name']
            team.id_category = category
            team.id_league = league
            team.save()
            football_category = Category.objects.get(name='Football')
            basketball_category = Category.objects.get(name='Basketball')
            hockey_category = Category.objects.get(name='Ice Hockey')
            if category == football_category:
                return redirect('/football/players/' + str(league_id))
            if category == basketball_category:
                return redirect('/basketball/players/' + str(league_id))
            if category == hockey_category:
                return redirect('/hockey/players/' + str(league_id)) 
    return render(request,'base/create_team.html',context)

def create_player(request, category_id, league_id, team_id):
    context = {
        'title': 'Create Player'
    }
    category = Category.objects.get(id=category_id)
    league = League.objects.get(id=league_id)
    team = Team.objects.get(id=team_id)
    if request.method == 'POST':
        if 'form1' in request.POST:
            player = Player()
            player.name = request.POST['name']
            player.surname = request.POST['surname']
            birthdaydate_string = request.POST['birthdaydate']
            player.birthdate = timezone.make_aware(datetime.strptime(f"{birthdaydate_string}", "%Y-%m-%d"))
            player_history = PlayerHistory()
            player_history.start_date = timezone.now()
            transfer_date = request.POST['transferdate']
            player_history.end_date = timezone.make_aware(datetime.strptime(f"{transfer_date}", "%Y-%m-%d"))
            player_history.id_team = team
            player_history.id_player = player
            player.save()
            player_history.save()
            football_category = Category.objects.get(name='Football')
            basketball_category = Category.objects.get(name='Basketball')
            hockey_category = Category.objects.get(name='Ice Hockey')
            if category == football_category:
                return redirect('/football/players/' + str(league_id) + '/' + str(team_id))
            if category == basketball_category:
                return redirect('/basketball/players/' + str(league_id) + '/' + str(team_id))
            if category == hockey_category:
                return redirect('/hockey/players/' + str(league_id) + '/' + str(team_id)) 
    return render(request,'base/create_player.html',context)

def delete_league(request, league_id):
    league = League.objects.get(id = league_id)
    league.delete()
    football_category = Category.objects.get(name='Football')
    basketball_category = Category.objects.get(name='Basketball')
    hockey_category = Category.objects.get(name='Ice Hockey')
    if league.id_category == football_category:
        return redirect('/football/players')
    if league.id_category == basketball_category:
        return redirect('/basketball/players')
    if league.id_category == hockey_category:
        return redirect('/hockey/players')
    return redirect('/football/players')

def delete_team(request, team_id):
    team = Team.objects.get(id = team_id)
    team.delete()
    football_category = Category.objects.get(name='Football')
    basketball_category = Category.objects.get(name='Basketball')
    hockey_category = Category.objects.get(name='Ice Hockey')
    if team.id_category == football_category:
        return redirect('/football/players/' + str(team.id_league.id))
    if team.id_category == basketball_category:
        return redirect('/basketball/players/' + str(team.id_league.id))
    if team.id_category == hockey_category:
        return redirect('/hockey/players/' + str(team.id_league.id))
    return redirect('/football/players')

def edit_team(request, team_id):
    team = Team.objects.get(id= team_id)
    leagues = League.objects.all().filter(id_category = team.id_category)
    context = {
        'title': 'Edit Team',
        'leagues': leagues,
        'team': team
    }
    if request.method == 'POST':
        if 'form1' in request.POST:
            print(request.POST)

            team.name = request.POST['name']
            selected_league = leagues.get(id = request.POST['league'])
            team.id_league = selected_league
            team.save()
            football_category = Category.objects.get(name='Football')
            basketball_category = Category.objects.get(name='Basketball')
            hockey_category = Category.objects.get(name='Ice Hockey')
            if team.id_category == football_category:
                return redirect('/football/players/' + str(team.id_league.id))
            if team.id_category == basketball_category:
                return redirect('/basketball/players/' + str(team.id_league.id))
            if team.id_category == hockey_category:
                return redirect('/hockey/players/' + str(team.id_league.id)) 
    return render(request,'base/edit_team.html',context)

def delete_player(request, player_id):
    player = Player.objects.get(id = player_id)
    some_date = date.today()
    player_history = PlayerHistory.objects.filter(Q(start_date__lte=some_date) & Q(end_date__gte=some_date)).first()
    player.delete()
    football_category = Category.objects.get(name='Football')
    basketball_category = Category.objects.get(name='Basketball')
    hockey_category = Category.objects.get(name='Ice Hockey')
    if player_history.id_team.id_category == football_category:
        return redirect('/football/players/' + str(player_history.id_team.id_league.id) + '/' + str(player_history.id_team.id))
    if player_history.id_team.id_category == basketball_category:
        return redirect('/basketball/players/' + str(player_history.id_team.id_league.id)+ '/' + str(player_history.id_team.id))
    if player_history.id_team.id_category == hockey_category:
        return redirect('/hockey/players/' + str(player_history.id_team.id_league.id))
    return redirect('/football/players')

def edit_player(request, player_id):
    player = Player.objects.get(id=player_id)
    player_history = PlayerHistory.objects.filter(id_player=player_id)
    player_info = {'player': player, 'history': player_history}
    first_history = player_history.first()
    teams = None
    if first_history:
        teams = Team.objects.all().filter(id_category = first_history.id_team.id_category.id)
    context = {
        'title': 'Edit Player',
        'teams': teams,
        'player': player_info
    }
    if request.method == 'POST':
        if 'form1' in request.POST:
            print(request.POST)
            player.name = request.POST['name']
            player.surname = request.POST['surname']
            birthdaydate_string = request.POST['birthdaydate']
            player.birthdate = timezone.make_aware(datetime.strptime(f"{birthdaydate_string}", "%Y-%m-%d"))
            player.save()
            PlayerHistory.objects.filter(id_player=player_id).delete()
            for i in range(0, len(request.POST.getlist('league'))):
                if request.POST.getlist('league')[i] == -1:
                    continue
                phistory = PlayerHistory()
                team = request.POST.getlist('league')[i]
                if team.isdigit():
                    phistory.id_team = Team.objects.get(id=team)
                    phistory.id_player = player
                    transferdates = request.POST.getlist('transferdate')
                    if i*2 < len(transferdates):
                        transfer_start_date = transferdates[i*2]
                    if i*2 + 1 < len(transferdates):
                        transfer_end_date = transferdates[i*2 + 1]
                    phistory.start_date = timezone.make_aware(datetime.strptime(f"{transfer_start_date}", "%Y-%m-%d"))
                    phistory.end_date = timezone.make_aware(datetime.strptime(f"{transfer_end_date}", "%Y-%m-%d"))
                    phistory.save()
            
    return render(request,'base/edit_player.html',context)