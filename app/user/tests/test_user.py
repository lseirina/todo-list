"""
Tests for user.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

REGISTER_URL = reverse('user:register')
LOGIN_URL = reverse('user:login')
HOME_URL = reverse('todo-home')

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
        res = self.client.post(REGISTER_URL, payload, follow=True)

        self.assertRedirects(res, LOGIN_URL)
        user = User.objects.filter(username=payload['username'])
        self.assertTrue(user.exists())

    def test_create_user_bad_credentials(self):
        """Test creating user with blank name is error."""
        payload = {
            'username': '',
            'password1': 'test123',
            'password2': 'testpass123',
        }
        res = self.client.post(REGISTER_URL, payload, follow=True)

        self.assertRedirects(res, REGISTER_URL)

    def test_create_user_blank_password(self):
        """Test creating user with blank password is error."""
        payload = {
            'username': 'Test Name',
            'password1': '',
            'password2': '',
        }

        res = self.client.post(REGISTER_URL, payload, follow=True)

        self.assertRedirects(res, REGISTER_URL)

    def test_login_user_success(self):
        """Tests user login is successful."""
        payload = {
            'username': 'Testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        res = self.client.post(LOGIN_URL, payload, follow=True)

        self.assertEqual(res.status_code, 200)


