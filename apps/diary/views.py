from django.views.generic.base import TemplateView
from .models import DiaryEntry
from django.http.response import HttpResponseRedirect
from datetime import datetime


DATE_FORMAT = '%Y-%m-%d'


class DatesView(TemplateView):
    template_name = 'dates_view.html'

    def get(self, request):
        context = {
            'entries': DiaryEntry.objects.filter(author=request.user)
        }
        return self.render_to_response(context)


class DiaryView(TemplateView):
    template_name = 'diary_page.html'

    def get(self, request, date=None):
        try:
            date = datetime.strptime(date or '', DATE_FORMAT)
        except ValueError:
            date = None

        if date:
            entry = DiaryEntry.objects.filter(
                author=request.user, date=date
            ).first()
            if entry:
                context = {
                    'note_date': entry.date,
                    'text': entry.text
                }
            else:
                context = {
                    'note_date': date,
                }
        else:
            context = {}

        return self.render_to_response(context)

    def post(self, request, date=None):
        date = request.POST.get('date')
        text = request.POST.get('text')

        try:
            date = datetime.strptime(date or '', DATE_FORMAT)
        except ValueError:
            return self.render_to_response({
                'errors': ['Incorrect date format!']
            })

        entry = DiaryEntry.objects.filter(
            author=request.user, date=date
        ).first()

        # if entry and entry.text:
        #     return self.render_to_response({
        #         'errors': [
        #             f'Date "{date.strftime(DATE_FORMAT)}" already exists and has text!'
        #         ],
        #         'text': text,
        #         'note_date': date,
        #     })

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text
            }
        )

        return HttpResponseRedirect(
            f'/diary/date-{date.strftime(DATE_FORMAT)}'
        )
