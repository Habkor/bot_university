# Generated by Django 4.0.3 on 2022-03-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decans', '0002_alter_decan_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='decan',
            name='patronymic',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Отчество'),
        ),
    ]