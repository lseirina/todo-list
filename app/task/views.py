"""Views for tasks."""
from django.shortcuts import render, redirect

from task.forms import FormTask
from core.models import Task

def task_view(request):
    if request.method == 'POST':
        form = FormTask(request, request.POST)
        if form.is_valid:
            form.save()
    else:
        form = FormTask()

    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})



















