from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'index2.html'


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/diary/all-dates/')

        return HttpResponseRedirect('/login')


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')

        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')

        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect('/signup')

        if User.objects.filter(email=email).exists():
            return HttpResponseRedirect('/signup')

        if password != password2:
            return HttpResponseRedirect('/signup')

        User.objects.create_user(
            username, email=email, password=password,
            first_name=firstname, last_name=lastname
        )

        return HttpResponseRedirect('/login')


class LogoutView(RedirectView):
    url = '/'

    def get(self, request):
        logout(request)
        return super().get(request)
