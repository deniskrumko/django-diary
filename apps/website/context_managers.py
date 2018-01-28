
def extra_context(request):
    return {
        'menu': (
            ('Create note', '/diary/'),
            ('Dates', '/diary/all-dates/'),
            ('Tags', '/tags/'),
        )
    }
