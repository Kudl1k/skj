from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('football/results', views.home, name="football"),
    path('football/results/<int:league_id>', views.home, name="football_league"),
    path('football/results/<int:league_id>/<int:match_id>', views.home, name="football_match"),
    path('football/players', views.players_football, name="football_players"),
    path('football/players/<int:league_id>', views.players_football, name="football_league_players"),
    path('football/players/<int:league_id>/<int:team_id>', views.players_football, name="football_team_players"),
    path('football/players/<int:league_id>/<int:team_id>/<int:player_id>', views.players_football, name="football_player_players"),
    path('login', views.login, name="login"),
    path('singup', views.signup, name="singup"),
    path('hockey/results', views.hockey, name="hockey"),
    path('hockey/results/<int:league_id>', views.hockey, name="hockey_league"),
    path('hockey/results/<int:league_id>/<int:match_id>', views.hockey, name="hockey_match"),
    path('basketball/results', views.basketball, name="basketball"),
    path('basketball/results/<int:league_id>', views.basketball, name="basketball_league"),
    path('basketball/results/<int:league_id>/<int:match_id>', views.basketball, name="basketball_match"),
]
