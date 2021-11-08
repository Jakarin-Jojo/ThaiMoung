from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('detail/<int:pk>/', views.DetailForumView.as_view(), name='detail'),
    path('create_forum/', views.create_forum, name='create_forum'),
]
