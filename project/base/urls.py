from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add-match-favourite/<int:match_id>',views.favourite_match,name='favourite_match'),
    path('', views.home, name="home"),
    path('create-league/<int:category_id>', views.create_league, name="create_league"),
    path('delete-league/<int:league_id>', views.delete_league, name="delete_league"),
    path('create-team/<int:category_id>/<int:league_id>', views.create_team, name="create_team"),
    path('delete-team/<int:team_id>', views.delete_team, name="delete_team"),
    path('edit-team/<int:team_id>', views.edit_team, name="edit_team"),
    path('create-player/<int:category_id>/<int:league_id>/<int:team_id>', views.create_player, name="create_player"),
    path('delete-player/<int:player_id>',views.delete_player,name="delete_player"),
    path('edit-player/<int:player_id>',views.edit_player,name="edit_player"),
    path('create-match/<int:category_id>/<int:league_id>', views.create_match, name="create_match"),
    path('edit-match/<int:match_id>', views.edit_match, name="edit_match"),
    path('delete-match/<int:match_id>', views.delete_match, name="delete_match"),
    path('delete-match/<int:match_id>', views.home, name="delete_match"),
    path('football/results', views.home, name="football"),
    path('football/results/<int:league_id>', views.home, name="football_league"),
    path('football/results/<int:league_id>/<int:match_id>', views.home, name="football_match"),
    path('football/players', views.players_football, name="football_players"),
    path('football/players/<int:league_id>', views.players_football, name="football_league_players"),
    path('football/players/<int:league_id>/<int:team_id>', views.players_football, name="football_team_players"),
    path('football/players/<int:league_id>/<int:team_id>/<int:player_id>', views.players_football, name="football_player_players"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('signup', views.user_signup, name="singup"),
    path('hockey/results', views.hockey, name="hockey"),
    path('hockey/results/<int:league_id>', views.hockey, name="hockey_league"),
    path('hockey/results/<int:league_id>/<int:match_id>', views.hockey, name="hockey_match"),
    path('hockey/players', views.players_hockey, name="hockey_players"),
    path('hockey/players/<int:league_id>', views.players_hockey, name="hockey_league_players"),
    path('hockey/players/<int:league_id>/<int:team_id>', views.players_hockey, name="hockey_team_players"),
    path('hockey/players/<int:league_id>/<int:team_id>/<int:player_id>', views.players_hockey, name="hockey_player_players"),
    path('basketball/results', views.basketball, name="basketball"),
    path('basketball/results/<int:league_id>', views.basketball, name="basketball_league"),
    path('basketball/results/<int:league_id>/<int:match_id>', views.basketball, name="basketball_match"),
    path('basketball/players', views.players_basketball, name="basketball_players"),
    path('basketball/players/<int:league_id>', views.players_basketball, name="basketball_league_players"),
    path('basketball/players/<int:league_id>/<int:team_id>', views.players_basketball, name="basketball_team_players"),
    path('basketball/players/<int:league_id>/<int:team_id>/<int:player_id>', views.players_basketball, name="basketball_player_players")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
