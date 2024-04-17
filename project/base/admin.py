from django.contrib import admin
from .models import User,Match,Category,Team,EditHistory,Favourite,Player, PlayerHistory, League

# Register your models here.

admin.site.register(User)
admin.site.register(Match)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(EditHistory)
admin.site.register(Favourite)
admin.site.register(Player)
admin.site.register(PlayerHistory)
admin.site.register(League)