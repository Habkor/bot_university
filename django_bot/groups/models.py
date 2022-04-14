from django.db import models
from django_bot.faculties.models import Faculty


class Group(models.Model):
    """Модель с группой"""

    group_name = models.CharField(
        max_length=255,
        verbose_name='Имя группы',
        default=None,
        null=True,
    )

    faculty = models.ForeignKey(
        Faculty,
        verbose_name='Факультет',
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        return f'{self.group_name}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
