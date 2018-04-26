from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    # Django Admin
    url(r'^admin/', admin.site.urls),

    # Index page
    url('', include('apps.website.urls', namespace='main')),

    # Apps
    url(r'^diary/', include('apps.diary.urls', namespace='diary')),
    url(r'^user/', include('apps.users.urls', namespace='users')),
]
