from django.conf.urls import url

from .views import UserSettingsView

urlpatterns = [
    url(
        r'^settings/$',
        UserSettingsView.as_view(),
        name='settings'
    ),
]
