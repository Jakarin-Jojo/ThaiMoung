from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('create_forum/', views.CreateForumView.as_view(), name='create_forum'),
]
