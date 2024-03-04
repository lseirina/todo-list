from django.urls import path

from task.views import task_view

app_name = 'task'

urlpatterns = [
    path('tasks/', task_view, name='task-list')
]