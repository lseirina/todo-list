"""Views for tasks."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from task.forms import TaskForm, TaskDetailForm
from core.models import Task

@login_required
def task_list(request):
    """Retrieve the list of tasks."""
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    """Retrieve task with description."""
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskDetailForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'The task is created.')
            return redirect('task:task-detail', task_id=task.id)
    else:
        form = TaskDetailForm()
    return render(request, 'task_create.html', {'form': form})

def task_update(request, pk):
    """Create a new task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskDetailForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task is changed.')
            return redirect('task:tasks-list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error: {error} in {field}')
                    return redirect('task:task-update', pk=pk)
    else:
        form = TaskDetailForm(instance=task)
    return render(request, 'task_update.html', {'form': form})
@login_required
def task_delete(request, pk):
    """Delete task."""
    task = get_object_or_404(Task, pk=pk)
    if task.user != request.user:
        return HttpResponseForbidden('You don`t have permition to delete this task.')
    if request.method == 'POST':
        task.delete()
        return redirect('task:tasks-list')
    return render(request, 'task_delete.html', {'task': task})



























