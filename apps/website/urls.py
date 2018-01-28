from django.conf.urls import url

from .views import IndexView, LoginView, LogoutView, SignUpView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
]
