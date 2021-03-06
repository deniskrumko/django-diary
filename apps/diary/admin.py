from django.contrib import admin
from import_export.admin import ImportExportMixin

from .import_export.resources import DiaryEntryResource
from .models import DiaryEntry


@admin.register(DiaryEntry)
class DiaryEntryAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin class for ``DiaryEntry`` model."""
    resource_class = DiaryEntryResource
    list_display = (
        'author',
        'date',
    )
