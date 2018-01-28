from django.views.generic.base import TemplateView
from .models import DiaryEntry
from django.http.response import HttpResponseRedirect


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

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text
            }
        )

        return HttpResponseRedirect(f'/diary/date-{date}')
