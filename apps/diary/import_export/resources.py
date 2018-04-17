from import_export import resources

from ..models import DiaryEntry


class DiaryEntryResource(resources.ModelResource):

    class Meta:
        model = DiaryEntry
