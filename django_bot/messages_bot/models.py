from django.db import models
from django_bot.faculties.models import Faculty
from django_bot.groups.models import Group


class Message(models.Model):
    """Модель сообщения для отправки сообщения"""

    text_message = models.TextField(
        verbose_name='Текст сообщения',
    )

    faculty_sending = models.ForeignKey(
        Faculty,
        max_length=10,
        verbose_name='Для какого факультета отправить уведомление',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    group_sending = models.ForeignKey(
        Group,
        max_length=10,
        verbose_name='Для какой группы отправить уведомление',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    is_all_sending = models.BooleanField(
        verbose_name='Отправить для всех',
        default=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.text_message[0:100]}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
