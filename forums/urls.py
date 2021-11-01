from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('base/', views.base, name='base'),
]
