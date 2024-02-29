from django.contrib import admin
from .models import Room, Question, Option
from unfold.admin import ModelAdmin


@admin.register(Room)
class Room(ModelAdmin):
    pass
@admin.register(Question)
class Questions(ModelAdmin):
    pass
@admin.register(Option)
class Option(ModelAdmin):
    pass