from django.contrib.auth import login, logout
# from django.contrib.auth.views import logout  если неработает заменить на это
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import View

from batyr.models import News


def homepage(request):
    news = News.objects.all()
    return render(request, 'news.html', locals())  # заменить locals на context


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = 'login.html'

    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
