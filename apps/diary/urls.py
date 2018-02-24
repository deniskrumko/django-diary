from django.conf.urls import url

from .views import DatesView, DiaryView, SearchView

urlpatterns = [
    url(
        r'^$',
        DiaryView.as_view(),
        name='date'
    ),
    url(
        r'^date-(?P<date>[\w-]+)/$',
        DiaryView.as_view(),
        name='date'
    ),
    url(
        r'^all-dates/$',
        DatesView.as_view(),
        name='dates'
    ),
    url(
        r'^search/$',
        SearchView.as_view(),
        name='search'
    ),
]
