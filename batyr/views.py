from django.contrib.auth import login, logout
# from django.contrib.auth.views import logout  если неработает заменить на это
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView

from batyr.forms import CommentForm
from batyr.models import News, Comment, CommentCategory
from batyr.serializer import CommentSerializer


def homepage(request):
    comment_category = CommentCategory.objects.all()
    comment = Comment.objects.all()
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


class CommentApi(APIView):

    def get(self, request):
        model = Comment.objects.all()
        serializer = CommentSerializer(model, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request):
        review = CommentSerializer(data=request.data)
        if review.is_valid():
            review.save()
        else:
            print('невалидны')
        return Response(status=201)
