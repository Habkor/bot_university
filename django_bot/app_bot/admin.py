from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import admin


admin.site.unregister(Group)
admin.site.unregister(User)
