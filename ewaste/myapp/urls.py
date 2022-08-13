from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='myapp'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("login", views.login, name='login'),
    path("loginall", views.loginall, name='loginall'),
    path("form_edonator", views.form_edonator, name='form_edonator'),
]
