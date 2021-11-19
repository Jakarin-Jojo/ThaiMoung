from django.utils import timezone

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import Post


class MainView(ListView):
    model = Post
    template_name = 'forums/main.html'

    def get_queryset(self):
        """Return: the last five published questions."""
        return Post.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')


# class CreateForumView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'forums/create_forum.html'


class DetailForumView(DetailView):
    model = Post
    template_name = 'forums/detail.html'


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


def search_post(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched == '':
            return redirect('main')
        post = Post.objects.filter(title__contains=searched)
        return render(request, 'event/search_post.html', {'searched': searched, 'post': post})
    else:
        return render(request, 'event/search_post.html', {})


def filter_category(request, cate):  # cate = News, Sport, ...
    category_posts = Post.objects.filter(category=cate)
    return render(request,
                  'event/categories.html',
                  {'cate': cate, 'category_post': category_posts})


@login_required(login_url='/accounts/login')
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    is_disliked = False

    for dislike in post.dislike.all():
        if dislike == request.user:
            is_disliked = True

    if is_disliked:
        post.dislike.remove(request.user)

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
def dislike_post(request, pk):
    post = Post.objects.get(pk=pk)

    is_liked = False

    for like in post.likes.all():
        if like == request.user:
            is_liked = True
            break

    if is_liked:
        post.likes.remove(request.user)

    is_dislike = False

    for dislike in post.dislike.all():
        if dislike == request.user:
            is_dislike = True
            break

    if is_dislike:
        post.dislike.remove(request.user)
    else:
        post.dislike.add(request.user)
    return redirect('detail', pk)
