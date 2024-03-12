"""Test for task."""
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from core.models import Task

TASKS_URL = reverse('task:task-list')

def detail_url(task_id):
    """Url for task detail."""
    return reverse('task:tas-detail', args=[task_id])

def create_user(**params):
    """Create and retuen a new user."""
    return User.objects.create_user(**params)

def create_task(user, **params):
    """Create a new task."""
    defaults = {'name': 'Task1'}
    defaults.update(params)

    task = Task.objects.create(user=user, **defaults)
    return task

class PublicTaskTests(TestCase):
    """Test unauthenticated requests."""

    def setUp(self):
        self.client = Client()

    def test_auth_required(self):
        """Test auth required to call web."""
        res = self.client.get(TASKS_URL)

        self.assertEqual(res.status_code, 401)

class PrivateTaskTests(TestCase):
    """Test authenticated requests."""

    def setUp(self):
        self.client = Client()
        self.user = create_user(
            username='Testname',
            password1='testpass123',
            password2='testpass123',
        )
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        """Test retrieving a list of tasks."""
        create_task(user=self.user)
        create_task(user=self.user)
        res = self.client.get(TASKS_URL)

        tasks = Task.objects.all().order_by('-id')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, tasks.data)

    def test_task_limited_to_user(self):
        """Test list of tasks limited to authenticated user."""
        user1 = User.objects.create_user(
            username='Testname2',
            password1='testpass123',
            password2='testpass123',
        )
        task1 = create_task(user=self.user)
        task2 = create_task(user=user1)

        res = self.client.get(TASKS_URL)

        task =  Task.objects.filter(user=self.user)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, task.data)