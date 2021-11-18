from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from forums.models import Post
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile


def edit_profile(request, username):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('main')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/edit_profile.html', context)


def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.warning(request, 'Please login.')
        return redirect('register_user')
    post_user = Post.objects.filter(user=user)
    user_profile = Profile.objects.get(user=user)
    user_profile.save()
    context = {'user_profile': user_profile, 'user_post': user, 'post_user': post_user}
    return render(request, 'users/profile.html', context)
