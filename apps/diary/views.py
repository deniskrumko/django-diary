from django.views.generic.base import TemplateView
from .models import DiaryEntry
from django.http.response import HttpResponseRedirect
from datetime import datetime, date
from django.utils import timezone
from dateutil.rrule import rrule, DAILY

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


class DatesView(TemplateView):
    template_name = 'dates_view.html'

    def get(self, request):
        current_year = timezone.now().year

        a = date(current_year, 1, 1)
        b = date(current_year, 12, 31)

        months = {}

        for dt in rrule(DAILY, dtstart=a, until=b):
            months.setdefault(month_names(dt.month), [])

            months[month_names(dt.month)].append(
                (dt, DiaryEntry.objects.filter(
                    author=request.user, date=dt
                ).exclude(text="").exists())
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
            'current_month': month_names(timezone.now().month)
        }
        return self.render_to_response(context)


class DiaryView(TemplateView):
    template_name = 'diary_page.html'

    def redirect_to_current_day(self):
        now = timezone.now()
        url = f'/diary/date-{now.strftime(DATE_FORMAT)}'
        return HttpResponseRedirect(url)

    def get_entry_date(self, entry):
        return entry.date.strftime(DATE_FORMAT) if entry else None

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

        context = {
            'note_date': entry.date,
            'text': entry.text,
            'prev_date': (entry.date - timezone.timedelta(days=1)),
            'next_date': (entry.date + timezone.timedelta(days=1)),
        }

        return self.render_to_response(context)

    def post(self, request, date=None):
        text = request.POST.get('text')

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text
            }
        )

        return HttpResponseRedirect(f'/diary/date-{date}')
