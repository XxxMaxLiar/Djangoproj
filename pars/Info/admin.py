from django.contrib import admin

# Register your models here.
from Info.models import TodoItem

@admin.register
class ToDoItemAdmin(admin.ModelAdmin):
    pass
