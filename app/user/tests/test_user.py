"""
Tests for user.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

CREATE_USER_URL = reverse('user:create')
LOGIN_URL = reverse('user:login')
HOME_URL = reverse('home')

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

    def test_create_user_bad_credentials(self):
        """Test creating user with blank name is error."""
        payload = {
            'username': '',
            'password': 'test123',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertequal(res.status_code, 400)

    def test_create_user_blank_password(self):
        """Test creating user with blank password is error."""
        payload = {
            'username': 'Test Name',
            'password': '',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, 400)

    def test_login_user_success(self):
        """Tests user login is successful."""
        payload = {
            'username': 'Testuser',
            'password': 'testpass123',
        }
        res = self.client.post(LOGIN_URL, payload, follow=True)

        self.assertRedirects(res, HOME_URL)


