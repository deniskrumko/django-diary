from django.views.generic.base import TemplateView
from .models import DiaryEntry
from django.http.response import HttpResponseRedirect
from datetime import datetime
from django.utils import timezone


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

    def redirect_to_current_day(self):
        now = timezone.now()
        url = f'/diary/date-{now.strftime(DATE_FORMAT)}'
        return HttpResponseRedirect(url)

    def get(self, request, date=None):
        if not date:
            return self.redirect_to_current_day()

        try:
            date = datetime.strptime(date or '', DATE_FORMAT)
        except ValueError:
            date = None

        if not date:
            return self.redirect_to_current_day()

        entry, created = DiaryEntry.objects.get_or_create(
            author=request.user, date=date,
            defaults={'text': ''}
        )

        prev_entry = DiaryEntry.objects.filter(date__lt=date).first()
        next_entry = DiaryEntry.objects.filter(date__gt=date).last()

        context = {
            'note_date': entry.date,
            'text': entry.text,
            'prev_date': prev_entry.date.strftime(DATE_FORMAT) if prev_entry else None,
            'next_date': next_entry.date.strftime(DATE_FORMAT) if next_entry else None,
        }

        return self.render_to_response(context)

    def post(self, request, date=None):
        date = request.POST.get('date')
        text = request.POST.get('text')

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text
            }
        )

        return HttpResponseRedirect(f'/diary/date-{date}')
