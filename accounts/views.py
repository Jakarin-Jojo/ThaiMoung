from django.shortcuts import render,redirect
from django.contrib.auth.models import User


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
        return redirect('main')
