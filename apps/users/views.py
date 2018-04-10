from django.views.generic.base import TemplateView

from apps.website.themes import THEMES


class UserSettingsView(TemplateView):
    template_name = 'settings.html'

    def get(self, request):
        user = self.request.user
        current_theme = None

        if user.settings:
            theme = user.settings.get('theme')

            if theme:
                current_theme = theme

        context = {
            'current_theme': current_theme,
            'themes': THEMES,
            'title': 'Django Diary - Настройки'
        }

        return self.render_to_response(context)

    def post(self, request):
        theme = request.POST.get('theme')

        if theme and theme in THEMES.keys():
            user = self.request.user
            user.settings['theme'] = theme
            user.save()

        return self.get(request)
