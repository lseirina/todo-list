"""Views for tasks."""
from django.shortcuts import render, redirect

from task.forms import FormTask

def task_view(request):
    if request.method == 'POST':
        request_form = FormTask(request)
        if request_form.is_valid:
            request_form.save()
            return redirect('task.html', args=['id'])



















