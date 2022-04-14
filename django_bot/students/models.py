from django.db import models
from django_bot.groups.models import Group


class Student(models.Model):
    """Класс студента."""

    chat_id = models.CharField(
        max_length=255,
        verbose_name='chat_id',
        default=None,
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )

    surname = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
    )

    patronymic = models.CharField(
        max_length=255,
        verbose_name='Отчество',
        default=None,
        null=True,
    )

    is_headman = models.BooleanField(
        default=False,
        verbose_name='Староста',
    )

    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
