"""
Tests for user.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

CREATE_USER_URL = reverse('user:create')

class PublicUserTest(TestCase):
    """Tests for not registrated user."""

    def setUp(self):
        self.client = Client()

    def test_create_user_success(self):
        """Test to create user is successfull."""
        payload = {
             'username': 'Test Name',
             'password': 'testpass123',
         }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, 201)
        user = User.objects.get(username=payload['username'])
        self.assertTrue(user.check_password, payload['password'])