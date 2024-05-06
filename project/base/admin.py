from django.contrib import admin
from .models import Match,Category,Team,GoalHistory,Favourite,Player, PlayerHistory, League

# Register your models here.

admin.site.register(Match)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(GoalHistory)
admin.site.register(Favourite)
admin.site.register(Player)
admin.site.register(PlayerHistory)
admin.site.register(League)