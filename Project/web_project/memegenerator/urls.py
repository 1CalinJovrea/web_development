from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='indexh'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    url(r'^oauth/', include('social_django.urls', namespace='social'))
]