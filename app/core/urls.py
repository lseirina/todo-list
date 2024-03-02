"""URL for home page."""
from django.urls import path
from core import views

name_app ='core'

urlpattern = [
    path('', views.homw_view, name='home')
]