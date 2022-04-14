from django.contrib import admin
from django_bot.messages_bot.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Регистрируем модель с сообщениями в админке"""
    ...
