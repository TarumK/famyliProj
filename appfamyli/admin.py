from django.contrib import admin
from .models import Town, Team, SubTeam

# Register your models here.

admin.site.register(Town)
admin.site.register(Team)
admin.site.register(SubTeam)