from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('football', views.home, name="football"),
    path('football/<str:league_id>', views.home, name="football_league"),
    path('football/<str:league_id>/<str:match_id>', views.home, name="football_match"),
    path('login', views.login, name="login"),
    path('singup', views.signup, name="singup"),
    path('hockey', views.hockey, name="hockey"),
    path('hockey/<str:league_id>', views.hockey, name="hockey_league"),
    path('hockey/<str:league_id>/<str:match_id>', views.hockey, name="hockey_match"),
    path('basketball', views.basketball, name="basketball"),
    path('basketball/<str:league_id>', views.basketball, name="basketball_league"),
    path('basketball/<str:league_id>/<str:match_id>', views.basketball, name="basketball_match"),

]
