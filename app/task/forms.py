"""Form for tasks."""
from django import forms
from core.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id', 'name']
        read_only_fields = ['id']

class TaskDetailForm(TaskForm):
    class meta(TaskForm.Meta):
        fields = TaskForm.Meta.fields + ['description']
