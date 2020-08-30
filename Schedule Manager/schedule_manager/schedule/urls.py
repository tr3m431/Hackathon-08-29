from django.urls import path

from . import views

urlpatterns = [
    path('', views.public_home_page, name='public_home_page'),
    path('/signup', views.login_page, name='login_page'),
]
