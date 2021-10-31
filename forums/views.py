from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from .models import Post


def main(request):
    return render(request, 'forums/main.html')


def sign_in_and_sign_up(request):
    return render(request, 'forums/sign_in_and_sign_up.html')


class CreateForumView(CreateView):
    model = Post
    template_name = 'forums/create_forum.html'
    fields = '__all__'
