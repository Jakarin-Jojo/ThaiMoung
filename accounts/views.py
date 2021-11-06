from django.shortcuts import render


def sign_in_and_sign_up(request):
    return render(request, 'accounts/sign_in_and_sign_up.html')
