from django.urls import reverse_lazy

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


class MainView(ListView):
    model = Topic
    template_name = 'forums/main.html'

    def get_queryset(self):
        """Return: the last five published questions."""
        return Topic.objects.filter(
            topic_date__lte=timezone.now()
        ).order_by('-topic_date')


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
            return filter_topic(request, event.topic)
    else:
        form = PostForm()
    return render(request, 'forums/create_forum.html', {'form': form})


class CreateComment(CreateView):
    model = Comment
    form_class = PostCommentForm
    template_name = 'forums/create_comment.html'

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs.get("pk")})


class CreateReply(CreateView):
    model = Reply
    form_class = PostReplyForm
    template_name = 'forums/create_reply.html'

    def form_valid(self, form):
        form.instance.comment = Comment.objects.get(pk=self.kwargs.get("pk_comment"))
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs.get("pk")})


# @login_required(login_url='/accounts/login')
# def create_comment(request, pk):
#     """Create a new comment.
#     Returns:
#     HttpResponseObject -- new event comment
#     """
#     if request.method == 'POST':
#         post = Post.objects.get(pk=pk)
#         comment_form = PostCommentForm(request.POST, request.FILES)
#         if comment_form.is_valid():
#             comment_form.post = post
#             comment_form.user = request.user
#             try:
#                 event = comment_form.save()
#             except IntegrityError:
#                 return redirect('main')
#             event.user = request.user
#             event.save()
#             return redirect('detail', pk=pk)
#     else:
#         comment_form = PostCommentForm()
#     return render(request, 'forums/detail.html', {'comment_form': comment_form})


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


@login_required(login_url='/accounts/login')
def likes_comment(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    is_disliked = False

    for dislike in comment.dislikes.all():
        if dislike == request.user:
            is_disliked = True

    if is_disliked:
        comment.dislikes.remove(request.user)

    is_liked = False

    for like in comment.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect('detail', pk)


@login_required(login_url='/accounts/login')
def dislikes_comment(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    is_liked = False

    for like in comment.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        comment.likes.remove(request.user)

    is_dislike = False

    for dislike in comment.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break

    if is_dislike:
        comment.dislikes.remove(request.user)
    else:
        comment.dislikes.add(request.user)
    return redirect('detail', pk)


@login_required(login_url='/accounts/login')
def likes_reply(request, pk, comment_pk, reply_pk):
    reply = Reply.objects.get(pk=reply_pk)
    is_disliked = False

    for dislike in reply.dislikes.all():
        if dislike == request.user:
            is_disliked = True

    if is_disliked:
        reply.dislikes.remove(request.user)

    is_liked = False

    for like in reply.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        reply.likes.remove(request.user)
    else:
        reply.likes.add(request.user)
    return redirect('detail', pk)


@login_required(login_url='/accounts/login')
def dislikes_reply(request, pk, comment_pk, reply_pk):
    reply = Reply.objects.get(pk=reply_pk)
    is_liked = False

    for like in reply.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        reply.likes.remove(request.user)

    is_dislike = False

    for dislike in reply.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break

    if is_dislike:
        reply.dislikes.remove(request.user)
    else:
        reply.dislikes.add(request.user)
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
    category_topic = Topic.objects.filter(category=cate).filter(
        topic_date__lte=timezone.now()
    ).order_by('-topic_date')
    return render(request,
                  'event/categories.html',
                  {'cate': cate, 'category_topic': category_topic})


def filter_topic(request, topic):
    topic_post = Post.objects.filter(topic=topic).filter(
        post_date__lte=timezone.now()
    ).order_by('-post_date')
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
