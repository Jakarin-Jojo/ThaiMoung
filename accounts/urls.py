from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in_and_sign_up, name='sign_in_and_sign_up'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
