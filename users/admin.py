from django.contrib import admin
from .models import UserProfile
from unfold.admin import ModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass
