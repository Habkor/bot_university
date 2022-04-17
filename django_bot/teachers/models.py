from django.db import models
from django_bot.faculties.models import Faculty
from django_bot.groups.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_bot.core.bot import updater
from django_bot.students.models import Student
from telegram.constants import PARSEMODE_HTML


class Teacher(models.Model):
    """Модель учителя в универе."""

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
        return f'{self.faculty} {self.name} {self.surname} {self.patronymic}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class MessageTeacher(models.Model):
    """Рассылка от преподавателя."""

    message = models.TextField(
        verbose_name='Ваше сообщение для студентов',
        help_text='Вы можете отослать сообщение для какой-то конкретной группы. '''
                  'ВНИМАНИЕ! При сохранении рассылки отправится сообщение всем студентам'
    )

    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'{self.message[0:100]}'

    class Meta:
        verbose_name = "Рассылка для преподавателя"
        verbose_name_plural = 'Рассылка'


@receiver(post_save, sender=MessageTeacher, dispatch_uid="update_stock_count")
def send_message_for_students(sender, instance, **kwargs):
    students = Student.objects.filter(
        group=instance.group
    )

    for student in students:
        updater.bot.send_message(
            student.chat_id,
            instance.message,
            parse_mode=PARSEMODE_HTML
        )
