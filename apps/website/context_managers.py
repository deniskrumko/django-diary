
def extra_context(request):
    return {
        'menu': (
            ('Сегодня', '/diary/'),
            ('Календарь', '/diary/all-dates/'),
            ('Поиск', '/diary/search/')
            # ('Tags', '/tags/'),
        )
    }
