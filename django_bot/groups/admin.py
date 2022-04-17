from django.contrib import admin
from django_bot.groups.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Админка для регистрации группы."""

    list_filter = ('group_name', 'faculty',)
