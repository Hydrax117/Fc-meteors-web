from django.contrib import admin

# Register your models here.
from players.models import Player,match,Team,Officials

admin.site.register(Player)
admin.site.register(match)
admin.site.register(Team)
admin.site.register(Officials)