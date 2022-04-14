from django.db import models
from django_bot.faculties.models import Faculty


class Decan(models.Model):
    """Класс декана"""

    chat_id = models.CharField(
        max_length=255,
        null=True,
        verbose_name='chat_id',
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

    password = models.CharField(
        max_length=255,
        verbose_name='Пароль',
        unique=True,
    )

    faculty = models.ForeignKey(
        Faculty,
        verbose_name='Факультет',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Декан'
        verbose_name_plural = 'Деканы'
