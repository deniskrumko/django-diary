from django.conf.urls import url

from .views import CalendarView, EditorView, SearchView

urlpatterns = [
    url(
        r'^$',
        EditorView.as_view(),
        name='date'
    ),
    url(
        r'^date-(?P<date>[\w-]+)/$',
        EditorView.as_view(),
        name='date'
    ),
    url(
        r'^all-dates/$',
        CalendarView.as_view(),
        name='dates'
    ),
    url(
        r'^search/$',
        SearchView.as_view(),
        name='search'
    ),
]
