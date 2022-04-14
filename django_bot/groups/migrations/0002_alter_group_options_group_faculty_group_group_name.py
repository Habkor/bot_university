# Generated by Django 4.0.3 on 2022-03-06 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculties', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AddField(
            model_name='group',
            name='faculty',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='faculties.faculty', verbose_name='Факультет'),
        ),
        migrations.AddField(
            model_name='group',
            name='group_name',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Имя группы'),
        ),
    ]