from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def sign_in_and_sign_up(request):
    return render(request, 'accounts/sign_in_and_sign_up.html')


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=username).exists():
        return redirect('sign_in_and_sign_up')
    elif User.objects.filter(email=email).exists():
        return redirect('sign_in_and_sign_up')
    elif User.objects.filter(password=password).exists():
        return redirect('sign_in_and_sign_up')
    else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return login(request)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is None:
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('main')
    else:
        return redirect('sign_in_and_sign_up')


def logout(request):
    auth.logout(request)
    return redirect('main')
