
def extra_context(request):
    return {
        'menu': (
            ('Today', '/diary/'),
            ('Calendar', '/diary/all-dates/'),
            # ('Tags', '/tags/'),
        )
    }
