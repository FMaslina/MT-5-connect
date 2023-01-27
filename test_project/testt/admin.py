from django.contrib import admin

# Register your models here.
from .models import BotUserModel


class BotUserModelAdmin(admin.ModelAdmin):
    list_display = (["id_bothelp"])


admin.site.register(BotUserModel, BotUserModelAdmin)