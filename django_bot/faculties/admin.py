from django.contrib import admin
from django_bot.faculties.models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    ...
