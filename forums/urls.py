from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create_forum/', views.CreateForumView.as_view(), name='create_forum'),
]
