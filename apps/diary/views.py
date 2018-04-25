from datetime import date, datetime

from dateutil.rrule import DAILY, rrule
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect, Http404
from django.utils import timezone
from django.views.generic.base import TemplateView, RedirectView

from .models import DiaryEntry

DATE_FORMAT = '%Y-%m-%d'


def month_names(index):
    maps = {
        1: 'Январь',
        2: 'Февраль',
        3: 'Март',
        4: 'Апрель',
        5: 'Май',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь',
    }
    return maps.get(index)


class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'calendar.html'
    login_url = '/login/'

    def get(self, request):
        current_year = timezone.now().year

        a = date(current_year, 1, 1)
        b = date(current_year, 12, 31)

        months = {}
        existing_entries = {
            entry.date: True if entry.date else False
            for entry in DiaryEntry.objects.filter(
                author=request.user,
            ).exclude(text="")
        }

        for dt in rrule(DAILY, dtstart=a, until=b):
            months.setdefault(month_names(dt.month), [])

            if dt.day == 1:
                for i in range(dt.weekday()):
                    months[month_names(dt.month)].append('-')

            months[month_names(dt.month)].append(
                (dt.date(), existing_entries.get(dt.date(), False))
            )

        last_days = [
            timezone.now() - timezone.timedelta(days=i)
            for i in range(0, 5)
        ]

        for index, day in enumerate(last_days):
            e = DiaryEntry.objects.filter(
                date=day, author=self.request.user
            ).first()
            last_days[index] = (day, bool(e.text if e else False))

        context = {
            'months': months,
            'last_days': last_days,
            'current_month': month_names(timezone.now().month),
            'current_day': timezone.now().day,
            'title': 'Django Diary - Даты',
        }
        return self.render_to_response(context)


class CurrentDayRedirectView(RedirectView):
    """View to redirect user to current day diary."""

    def get_redirect_url(self, *args, **kwargs):
        now = timezone.now()
        return f'/diary/date-{now.strftime(DATE_FORMAT)}'


class EntryPreviewView(LoginRequiredMixin, TemplateView):
    """View for diary entry preview."""
    template_name = 'entry_preview.html'
    login_url = '/login/'

    def get(self, request, date):
        try:
            date = datetime.strptime(date or '', DATE_FORMAT)
        except ValueError:
            raise Http404()

        entry, created = DiaryEntry.objects.get_or_create(
            author=request.user, date=date,
            defaults={'text': ''}
        )

        context = {
            'prev_date': (entry.date - timezone.timedelta(days=1)),
            'next_date': (entry.date + timezone.timedelta(days=1)),
            'entry': entry,
            'title': entry.date,
        }

        return self.render_to_response(context)


class EntryEditView(EntryPreviewView):
    template_name = 'entry_edit.html'
    login_url = '/login/'

    def post(self, request, date=None):
        text = request.POST.get('text')

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text
            }
        )

        messages.add_message(
            request, messages.SUCCESS, 'Дневник успешно сохранен!'
        )

        return HttpResponseRedirect(f'/diary/date-{date}')


class SearchView(TemplateView):
    """
    TODO
    1. Normal query in URL
    2. Pagination
    3. Message - not found
    """
    template_name = 'search.html'

    def get(self, request, search=None):
        context = self.get_context_data()

        context['results'] = DiaryEntry.objects.filter(
            text__iregex=search
        ) if search else None
        context['search'] = search
        context['title'] = 'Django Diary - Поиск'

        return self.render_to_response(context)

    def post(self, request):
        search = request.POST.get('search')
        return self.get(request, search=search)
