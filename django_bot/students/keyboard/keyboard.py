from django_bot.groups.models import Group


def get_keyboard_groups():
    groups = Group.objects.all()
    ...
