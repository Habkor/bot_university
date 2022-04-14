from django.db import models


class Faculty(models.Model):
    """Модель факультета."""

    name = models.CharField(
        max_length=255,
        verbose_name='Имя факультета'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'