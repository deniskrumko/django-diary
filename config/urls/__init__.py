from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('apps.website.urls')),
    url(r'^diary/', include('apps.diary.urls')),
]
