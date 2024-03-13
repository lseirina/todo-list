"""Test for task."""
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from core.models import Task


def create_user(**params):
    """Create and retuen a new user."""
    return User.objects.create_user(**params)

def create_task(user, **params):
    """Create a new task."""
    defaults = {'title': 'Task1'}
    defaults.update(params)

    task = Task.objects.create(user=user, **defaults)
    return task

class PublicTaskTests(TestCase):
    """Test unauthenticated requests."""

    def setUp(self):
        self.client = Client()

    def test_auth_required(self):
        """Test auth required to call web."""
        url = reverse('task:tasks-list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 302)

class PrivateTaskTests(TestCase):
    """Test authenticated requests."""

    def setUp(self):
        self.client = Client()
        self.user = create_user(
            username='Testname',
            password='testpass123',
        )
        self.client.force_login(self.user)

    def test_retrieve_tasks(self):
        """Test retrieving a list of tasks."""
        create_task(user=self.user)
        create_task(user=self.user)

        url = reverse('task:tasks-list')
        res = self.client.get(url)

        tasks = Task.objects.all().order_by('-id')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, tasks.title)

    def test_task_limited_to_user(self):
        """Test list of tasks limited to authenticated user."""
        user1 = User.objects.create_user(
            username='Testname2',
            password='testpass123',
        )
        task1 = create_task(user=self.user)
        task2 = create_task(user=user1)

        url = reverse('task:tasks-list')
        res = self.client.get(url)

        task =  Task.objects.filter(user=self.user)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, task.title)

    def test_get_task_detail(self):
        """Test get task detail."""
        task = create_task(user=self.user)

        url = reverse('task:task-detail', kwargs={'task_id': task.id})
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, task.title)

    def test_create_task(self):
        """Test creating a new task."""
        payload = {
            'title': 'Hard task',
            'description': 'Do this.',
        }

        url = reverse('task:task-create')
        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, 201)
        task = Task.objects.get(id=res.data[id])
        for k, v in payload.items():
            self.assertEqual(getattr(task, k), v)
        self.assertEqual(task.user, self.user)

    def test_partial_update(self):
        """Test partial update of the task."""
        original_title = 'Easy task.'
        task = create_task(
            user=self.user,
            title=original_title,
            description='Do that.'
        )
        payload = {'description': 'Do this.'}

        url = reverse('task:task-update', kwargs={'pk': task.pk})
        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, 200)
        task.refresh_from_db()
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.title, original_title)
        self.assetrtEqual(task.description, payload['description'])

    def test_full_update(self):
        """Test ful update of the task."""
        task = create_task(
            user=self.user,
            title='One more task.',
            description='Do it.',
        )
        payload = {
            'title': 'New Task',
            'description': 'Do it again.',
        }

        url = reverse('task:task-update', kwargs={'pk': task.pk})
        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, 200)
        task.refresh_from_db()
        for k, v in payload.items():
            self.assertEqual(getattr(task, k), v)
        self.assertEqual(task.user, self.user)

    def test_delete_task(self):
        """Test delete task."""
        task = create_task(user=self.user)

        url = reverse('task:task-delete', kwargs={'pk': task.pk})
        res = self.client.post(url)

        self.assertEqual(res.status_code, 204)
        self.assertFalse(Task.objects.filter(user=self.user).exists())


