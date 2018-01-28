from django.contrib import admin
from .models import DiaryEntry


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    """Admin class for ``DiaryEntry`` model."""
    list_display = (
        'author',
        'date',
    )
