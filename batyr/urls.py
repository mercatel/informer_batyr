"""informer_batyr URL Configuration

"""
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage_url'),
    path('cro/', include('cro.urls'), name='cro_url'),
    path('mk/', include('mk.urls'), name='mk_url'),
    path('login/', views.LoginFormView.as_view(), name='login_url'),
    path('logout/', views.LogoutView.as_view(), name='logout_url'),
]
