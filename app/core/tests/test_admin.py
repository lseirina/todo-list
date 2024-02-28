"""Test for django admin modification."""
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

class AdminSiteTest(TestCase):
    """Tests for listing users."""

    def setUp(self):
        self.adminuser = User.objects.create_superuser(
            username='Test Name',
            email='test@example.com',
            password='testpass123',
        )
        self.client = Client()
        self.client.force_login(self.adminuser)
        self.user = User.objects.create_user(
            username='User Name',
            password='test123',
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:auth_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse('admin:auth_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
