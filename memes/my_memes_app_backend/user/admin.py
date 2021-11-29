from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import User


class UserManager(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "is_superuser",
        "is_verify"
    ]


admin.site.register(User, UserManager)
