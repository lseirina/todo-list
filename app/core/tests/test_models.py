"""Test for models."""
from django.test import TestCase
from django.contrib.auth.models import User
from core import models


def create_user(username='Testname', password='testpass123'):
    """Create and return a new user."""
    return User.objects.create_user(username=username, password=password)


class ModelTest(TestCase):

    def test_create_task(self):
        """Test create task is succesful."""
        user = create_user()
        task = models.Task.objects.create(
            user=user,
            title='Test title',
        )

        self.assertEqual(str(task), task.title)
