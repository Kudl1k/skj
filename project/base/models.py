from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    score_1 = models.IntegerField(default=0)
    score_2 = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    viewers = models.IntegerField(default=0)
    stadium = models.CharField(max_length=30,default="")
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    id_league = models.ForeignKey('League', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_team_1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team_1')
    id_team_2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team_2')

    def __str__(self):
        return f'{self.id_category.name},{self.id_league.name} - {self.start_time} - {self.id_team_1.name} vs {self.id_team_2.name} ({self.score_1}:{self.score_2}) '


class Category(models.Model):
    name = models.CharField(max_length=30,default="",null=False)
    description = models.CharField(max_length=100,default="",null=True)

    def __str__(self):
        return f'{self.name}'

class League(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id_category.name})'

class Team(models.Model):
    name = models.CharField(max_length=30,default="",null=False)
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    id_league = models.ForeignKey('League', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id_category.name} - {self.id_league.name})'

class GoalHistory(models.Model):
    minute = models.IntegerField()
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.match.id_team_1.name} : {self.match.id_team_2.name} - {self.minute} - {self.player}'


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_match = models.ForeignKey('Match', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.id_match.id_team_1.name} vs {self.id_match.id_team_2.name} ({self.id_match.start_time})'

    class Meta:
        unique_together = ('user', 'id_match')

class Player(models.Model):
    name = models.CharField(max_length=20,blank=False,null=False)    
    surname = models.CharField(max_length=20,blank=False,null=False)
    birthdate = models.DateField(blank=False,null=False)
    
    def __str__(self):
        return f'{self.surname} {self.name} ({self.birthdate})'

class PlayerHistory(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    id_team = models.ForeignKey('Team', on_delete=models.CASCADE)
    id_player = models.ForeignKey('Player', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_team.name} - {self.id_player.surname} {self.id_player.name} ({self.start_date} -> {self.end_date})'