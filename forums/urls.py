from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('detail/<int:pk>/', views.DetailForumView.as_view(), name='detail'),
    path('detail/<int:pk>/like', views.likes_post, name='likes'),
    path('detail/<int:pk>/dislike', views.dislikes_post, name='dislikes'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('detail/<int:pk>/create_comment', login_required(views.CreateComment.as_view()), name='create_comment'),
    path('detail/<int:pk>/create_reply', login_required(views.CreateReply.as_view()), name='create_reply'),
    path('search/', views.search_topic, name='search'),
    path('category_<str:cate>/', views.filter_category, name='category'),
    path('category_<str:cate>/search', views.search_post_category, name='search_category'),
    path('topic_<str:topic>', views.filter_topic, name='topic'),
    path('topic_<str:topic>/search', views.search_post_topic, name='search_topic'),
    path('detail/<int:pk>/<int:comment_pk>/likes_comment', views.likes_comment, name='likes_comment'),
    path('detail/<int:pk>/<int:comment_pk>/dislikes_comment', views.dislikes_comment, name='dislikes_comment'),
]
