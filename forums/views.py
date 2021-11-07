from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .forms import PostForm

from .models import Post


def sign_in_and_sign_up(request):
    return render(request, 'forums/sign_in_and_sign_up.html')


class MainView(ListView):
    model = Post
    template_name = 'forums/main.html'


class CreateForumView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forums/create_forum.html'
