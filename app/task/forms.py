"""Form for tasks."""
from django import forms
from core.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id', 'title']
        read_only_fields = ['id']

class TaskDetailForm(TaskForm):
    class Meta(TaskForm.Meta):
        fields = TaskForm.Meta.fields + ['description']

