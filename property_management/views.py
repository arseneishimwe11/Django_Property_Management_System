from django.shortcuts import render, redirect
from django.contrib.auth import logout


def landing_page(request):
    return render(request, 'landing.html')


def logout_user(request):
    logout(request)
    return redirect('/users/login')
