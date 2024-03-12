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
        task1 = Task.objects.create(
            user=self.user,
            username='Task1',
        )
        task2 = Task.objects.create(
            user=self.user,
            username='Task2',
        )
        res = self.client.get(TASKS_URL)

        tasks = Task.objects.all().order_by('-id')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, tasks.data)
