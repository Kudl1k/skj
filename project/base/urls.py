from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('football', views.home, name="football"),
    path('login', views.login, name="login"),
    path('singup', views.signup, name="singup"),
    path('hockey', views.hockey, name="hockey"),
    path('basketball', views.basketball, name="basketball"),
]
