from django.shortcuts import reverse


def extra_context(request):
    return {
        'menu': (
            ('Сегодня', reverse('diary:current-day')),
            ('Календарь', reverse('diary:calendar')),
            ('Поиск', reverse('diary:search'))
            # ('Tags', '/tags/'),
        )
    }
