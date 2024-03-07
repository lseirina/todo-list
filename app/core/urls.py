"""URL for home page."""
from django.urls import path
from core import views

name_app ='core'

urlpatterns = [
    path('', views.home_view, name='todo-home')
]