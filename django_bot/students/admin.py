from django.contrib import admin
from django_bot.students.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'is_headman', 'group')
    list_filter = ('is_headman', )

    def has_add_permission(self, request):
        return False
