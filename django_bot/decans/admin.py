from django.contrib import admin
from django_bot.decans.models import Decan


@admin.register(Decan)
class DecanAdmin(admin.ModelAdmin):
    """Регистрируем декана в админке."""

    readonly_fields = ('chat_id', )
