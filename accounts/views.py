from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations! Successful account creation.')
            return redirect('register_user')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/sign_in_and_sign_up.html', {'form_register': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.warning(request, 'Username or Password is incorrect.')
    return redirect('register_user')


def logout_user(request):
    logout(request)
    return redirect('main')
