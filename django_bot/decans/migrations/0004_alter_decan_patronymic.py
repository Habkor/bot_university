# Generated by Django 4.0.3 on 2022-03-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decans', '0003_decan_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decan',
            name='patronymic',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Отчество'),
        ),
    ]
