"""URL mapping for the user."""

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.register_view, name='create')
]