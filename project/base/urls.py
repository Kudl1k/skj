from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('results/football', views.home, name="football"),
    path('results/football/<int:league_id>', views.home, name="football_league"),
    path('results/football/<str:league_id>/<str:match_id>', views.home, name="football_match"),
    path('players/football', views.players, name="football_players"),
    path('login', views.login, name="login"),
    path('singup', views.signup, name="singup"),
    path('results/hockey', views.hockey, name="hockey"),
    path('results/hockey/<str:league_id>', views.hockey, name="hockey_league"),
    path('results/hockey/<str:league_id>/<str:match_id>', views.hockey, name="hockey_match"),
    path('results/basketball', views.basketball, name="basketball"),
    path('results/basketball/<str:league_id>', views.basketball, name="basketball_league"),
    path('results/basketball/<str:league_id>/<str:match_id>', views.basketball, name="basketball_match"),
]
