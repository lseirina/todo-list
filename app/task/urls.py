from django.urls import path

from task import views

app_name = 'task'

urlpatterns = [
    path('tasks/<int:task_id>', views.task_detail, name='task-detail'),
    path('tasks/', views.task_list, name='tasks-list'),
    path('tasks/task_create', views.task_create, name='task-create'),
    path('tasks/task_update/<int:pk>', views.task_update, name='task-update'),
    path('tasks/delete/<int:pk>', views.task_delete, name='task-delete'),
]