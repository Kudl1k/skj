from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Match, EditHistory

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EditMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['start_time', 'stadium', 'viewers', 'id_team_1', 'score_1', 'id_team_2', 'score_2']

class AddMatchHistoryForm(forms.ModelForm):
    class Meta:
        model = EditHistory
        fields = ['id_match', 'new_score1', 'new_score2', 'modified_at', 'user']