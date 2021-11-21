from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('detail/<int:pk>/', views.DetailForumView.as_view(), name='detail'),
    path('detail/<int:pk>/like', views.likes_post, name='likes'),
    path('detail/<int:pk>/dislike', views.dislikes_post, name='dislikes'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('search/', views.search_topic, name='search'),
    path('category_<str:cate>/', views.filter_category, name='category'),
    path('category_<str:cate>/search', views.search_post_category, name='search_category'),
    path('topic_<str:topic>', views.filter_topic, name='topic'),
    path('topic_<str:topic>/search', views.search_post_topic, name='search_topic'),
]
