# Generated by Django 3.2.13 on 2022-04-17 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255, null=True, verbose_name='chat_id')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(default=None, max_length=255, null=True, verbose_name='Отчество')),
                ('password', models.CharField(max_length=255, unique=True, verbose_name='Пароль')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculties.faculty', verbose_name='Факультет')),
            ],
        ),
    ]
