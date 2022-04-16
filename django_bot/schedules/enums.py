from django.db import models


class DaysOfWeek(models.TextChoices):
    MONDAY = 'monday', 'Понедельник'
    TUESDAY = 'tuesday', 'Вторник'
    WEDNESDAY = 'wednesday', 'Среда'
    THURSDAY = 'thursday', 'Четверг'
    FRIDAY = 'friday', 'Пятница'
    SATURDAY = 'saturday', 'Суббота'


class OrderWeek(models.TextChoices):
    denominator = 'denominator', 'Знаменатель'
    numerator = 'numerator', 'Числитель'
