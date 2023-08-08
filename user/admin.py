from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from user.models import User


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ("email", )
