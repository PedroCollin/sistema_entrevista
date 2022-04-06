from django.contrib import admin
from .models import User

@admin.register(User)
class detUsuario(admin.ModelAdmin):
    list_display = ('nome', 'edv', 'email', 'password', 'foto')