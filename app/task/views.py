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

def task_create(request, pk):
    """Create a new task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskDetailForm(request.PORT, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'A new task created.')
            return redirect(request, 'task-list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error: {error} in {field}')
                    return redirect(request, 'task_update', {'form': form})
    else:
        form = TaskDetailForm(instance=task)
    return render(request, 'task_create.html', {'form': form})

def task_delete(request, pk):
    """Delete task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'rask_delete.html', {'task': task})



























