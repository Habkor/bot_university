from django.db import models
from django_bot.schedules.enums import DaysOfWeek
from django_bot.schedules.enums import OrderWeek
from django_bot.groups.models import Group


class ScheduleForStudent(models.Model):
    """Расписание для студентов"""

    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        null=True,
        on_delete=models.CASCADE
    )

    days_of_week = models.CharField(
        choices=DaysOfWeek.choices,
        verbose_name='День недели',
        max_length=255
    )

    text_schedule = models.TextField(
        verbose_name='Текст расписания'
    )

    order = models.CharField(
        choices=OrderWeek.choices,
        verbose_name='Числитель/Знаменатель',
        max_length=255
    )

    def __str__(self):
        return f'{self.text_schedule[0:100]}'

    class Meta:
        verbose_name = 'Рассписание для студента'
        verbose_name_plural = 'Рассписание для студента'

