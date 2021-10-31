from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'forums/main.html')


def sign_in_and_sign_up(request):
    return render(request, 'forums/sign_in_and_sign_up.html')
