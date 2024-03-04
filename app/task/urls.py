from django.urls import path

from task import views

app_name = 'task'

urlpatterns = [
    path('tasks/', views.task_view, name='tasks')
]