"""
Views for user.
"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.shortcuts import render, redirect

def register_view(request):
    """Generate form for user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def login_view(request):
    """Generate login for user."""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
        render(request, 'login.html', {'form': form})


def home_view(request):
    """Send authenticated user to home page."""
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return redirect('login')

