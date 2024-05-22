from django.contrib import admin
from .models import Room

# Register your models here.
@admin.register(Room)
class roomAdmin(admin.ModelAdmin):
    list_display = ("name","capacity",)
    search_fields = ('name','capacity','created_at',)
    ordering = ("created_at","reserved_for",)
    fields = ('name', 'reserved_for',)
