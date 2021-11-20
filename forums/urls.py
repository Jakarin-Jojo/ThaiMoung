from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('detail/<int:pk>/', views.DetailForumView.as_view(), name='detail'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('search/', views.search_post, name='search'),
    path('category_<str:cate>/', views.filter_category, name='category'),
    path('topic_<str:topic>', views.filter_topic, name='topic'),
    path('topic_<str:topic>/search', views.search_post_topic, name='search_topic'),
]
