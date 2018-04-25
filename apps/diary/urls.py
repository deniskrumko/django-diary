from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.CurrentDayRedirectView.as_view(),
        name='current-day'
    ),
    url(
        r'^date-(?P<date>[\w-]+)/$',
        views.EntryPreviewView.as_view(),
        name='entry-preview'
    ),
    url(
        r'^date-(?P<date>[\w-]+)/edit/$',
        views.EntryEditView.as_view(),
        name='entry-edit'
    ),
    url(
        r'^calendar/$',
        views.CalendarView.as_view(),
        name='calendar'
    ),
    url(
        r'^search/$',
        views.SearchView.as_view(),
        name='search'
    ),
]
