from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.base import RedirectView, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Django Diary - Главная'
        }

    def get(self, request):
        """Method redirects to calendar page if user is authenticated."""
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('diary:calendar'))

        return super().get(request)


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Django Diary - Вход'
        }

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('diary:calendar'))

        return HttpResponseRedirect(reverse('main:login'))


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Django Diary - Регистрация'
        }

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')

        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')

        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect(reverse('main:signup'))

        if User.objects.filter(email=email).exists():
            return HttpResponseRedirect(reverse('main:signup'))

        if password != password2:
            return HttpResponseRedirect(reverse('main:signup'))

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
