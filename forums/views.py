from django.utils import timezone

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from .forms import PostForm, PostTopicForm
from .models import Post, Topic


class MainView(ListView):
    model = Topic
    template_name = 'forums/main.html'

    def get_queryset(self):
        """Return: the last five published questions."""
        return Post.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')


class DetailForumView(DetailView):
    model = Post
    template_name = 'forums/detail.html'


@login_required(login_url='/accounts/login')
def create_topic(request):
    """Create a new topic.
    Returns:
    HttpResponseObject -- new event topic
    """
    if request.method == 'POST':
        topic_form = PostTopicForm(request.POST, request.FILES)
        if topic_form.is_valid():
            topic = topic_form.cleaned_data['topic_name']
            try:
                event = topic_form.save()
            except IntegrityError:
                messages.warning(request, f'Topic {topic} is already exists.')
                return redirect('main')
            event.user = request.user
            event.save()
            messages.success(request, f'{topic} has been created.')
            return redirect('main')
    else:
        topic_form = PostTopicForm()
    return render(request, 'forums/create_topic.html', {'topic_form': topic_form})


@login_required(login_url='/accounts/login')
def create_forum(request):
    """Create a new event.
    Returns:
    HttpResponseObject -- new event page
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            forum_title = form.cleaned_data['title']
            try:
                event = form.save()
            except IntegrityError:
                messages.warning(request, f'Forum {forum_title} is already exists.')
                return redirect('main')
            event.user = request.user
            event.save()
            messages.success(request, f'{forum_title} has been created.')
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'forums/create_forum.html', {'form': form})
    
    
@login_required(login_url='/accounts/login')
def likes_post(request, pk):
    post = Post.objects.get(pk=pk)
    is_disliked = False

    for dislike in post.dislikes.all():
        if dislike == request.user:
            is_disliked = True

    if is_disliked:
        post.dislikes.remove(request.user)

    is_liked = False

    for like in post.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('detail', pk)


@login_required(login_url='/accounts/login')
def dislikes_post(request, pk):
    post = Post.objects.get(pk=pk)

    is_liked = False

    for like in post.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        post.likes.remove(request.user)

    is_dislike = False

    for dislike in post.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break

    if is_dislike:
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return redirect('detail', pk)


def search_topic(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched == '':
            return redirect('main')
        topic = Topic.objects.filter(topic_name__contains=searched)
        return render(request, 'event/search_main_topic.html', {'searched': searched, 'topic': topic})
    else:
        return render(request, 'event/search_main_topic.html', {})


def filter_category(request, cate):  # cate = News, Sport, ...
    category_topic = Topic.objects.filter(category=cate)
    return render(request,
                  'event/categories.html',
                  {'cate': cate, 'category_topic': category_topic})


def filter_topic(request, topic):
    topic_post = Post.objects.filter(topic=topic)
    return render(request,
                  'event/posted_forum.html',
                  {'topic': topic, 'topic_post': topic_post})


def search_post_topic(request, topic):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched == '':
            return redirect('main')
        post = Post.objects.filter(topic=topic).filter(title__contains=searched)
        return render(request, 'event/search_post.html', {'searched': searched, 'post': post, 'topic': topic})
    else:
        return render(request, 'event/search_post.html', {})


def search_post_category(request, cate):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched == '':
            return redirect('main')
        topic = Topic.objects.filter(category=cate).filter(topic_name__contains=searched)
        return render(request, 'event/search_topic.html', {'searched': searched, 'topic': topic, 'cate': cate})
    else:
        return render(request, 'event/search_topic.html', {})
