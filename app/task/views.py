"""Views for tasks."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from task.forms import TaskForm, TaskDetailForm
from core.models import Task

def task_list(request):
    """Retrieve the list of tasks."""
    tasks = Task.objects.all()
    titles = [ task.title for task in tasks]
    return render(request, 'task_list.html', {'titles': titles})

def task_detail(request, task_id):
    """Retrieve task with description."""
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskDetailForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, 'The task is created.')
            return redirect('task-detail', task_id=task.id)
    else:
        form = TaskDetailForm()
    return render(request, 'task_detail.html', {'from': form})

def task_update(request, pk):
    """Create a new task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskDetailForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task is chenged.')
            return redirect('task-list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error: {error} in {field}')
                    return redirect('task_update', pk=pk)
    else:
        form = TaskDetailForm(instance=task)
    return render(request, 'task_create.html', {'form': form})

def task_delete(request, pk):
    """Delete task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'task_delete.html', {'task': task})



























