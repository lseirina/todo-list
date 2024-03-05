"""Views for tasks."""
from django.shortcuts import render, redirect

from task.forms import TaskForm
from core.models import Task

def task_view(request):
    if request.method == 'POST':
        form = TaskForm(request, request.POST)
        if form.is_valid:
            form.save()
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})



















