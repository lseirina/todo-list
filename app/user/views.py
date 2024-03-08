"""
Views for user.
"""
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.shortcuts import render, redirect

def register_view(request):
    """Generate form for user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully. Please log in')
            return redirect('user:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def login_view(request):
    """Generate login for user."""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #return HttpResponse('hello')
                return redirect('todo-home')
            else:
                return render(request, 'login.html', {'form': form, 'error message': 'invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    """Send authenticated user to home page."""
    if request.user.is_authenticated():
        return render(request, 'home.html')
    else:
        return redirect('login')

