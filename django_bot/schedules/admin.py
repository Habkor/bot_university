from django.contrib import admin
from django_bot.schedules.models import ScheduleForStudent


@admin.register(ScheduleForStudent)
class ScheduleForStudent(admin.ModelAdmin):

    list_display = (
        'days_of_week', 'text_schedule', 'group',
    )

