from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20,blank=False,null=False)
    email = models.CharField(max_length=50,blank=False,null=False)
    name = models.CharField(max_length=20,blank=False,null=False)
    surname = models.CharField(max_length=20,blank=False,null=False)
    street = models.CharField(max_length=30,blank=True,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    zip = models.CharField(max_length=6,blank=True,null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=20,blank=False,null=False)
    role = models.CharField(max_length=1,default='W',blank=False,null=False)
    last_log = models.DateTimeField(null=True,auto_now_add=True)
    created_at = models.DateTimeField(null=False,blank=False,auto_now_add=True)

    def __str__(self):
        return f'[{self.role}] {self.username} - {self.surname} {self.name}'

class Match(models.Model):
    score_1 = models.IntegerField(default=0)
    score_2 = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    viewers = models.IntegerField(default=0)
    stadium = models.CharField(max_length=30,default="")
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    id_league = models.ForeignKey('League', on_delete=models.CASCADE)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
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

class EditHistory(models.Model):
    modified_at = models.DateTimeField(null=True)
    old_score1 = models.IntegerField(default="",null=False)
    old_score2 = models.IntegerField(default="",null=False)
    new_score1 = models.IntegerField(default="",null=False)
    new_score2 = models.IntegerField(default="",null=False)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    id_match = models.ForeignKey('Match', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_match.id_team_1.name} vs {self.id_match.id_team_2.name} - ({self.id_user.username}) {self.modified_at} - {self.old_score1}:{self.old_score2} -> {self.new_score1}:{self.new_score2}'

class Favourite(models.Model):
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    id_match = models.ForeignKey('Match', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_user.username} - {self.id_match.id_team_1.name} vs {self.id_match.id_team_2.name} ({self.id_match.start_time})'

    class Meta:
        unique_together = ('id_user', 'id_match')

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