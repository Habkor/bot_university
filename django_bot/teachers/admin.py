from django.contrib import admin
from django_bot.teachers.models import Teacher
from django_bot.teachers.models import MessageTeacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    readonly_fields = ('chat_id', )


@admin.register(MessageTeacher)
class MessageTeacherAdmin(admin.ModelAdmin):
    ...
