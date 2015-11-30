from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.test import TestCase

# Create your tests here.
class SecretTestCase(TestCase):
    def setUp(self):
        self.username = "admin"
        self.user = User.objects.create_user(username="admin", password="password", email="activelime@yahoo.com")
        self.secret = self.user.secret_set.create(description="hello")

    def test_add_secret(self):
        self.assertTrue(User.objects.filter(pk=self.user.id))
        self.assertTrue(self.user.secret_set.filter(pk=self.secret.id).exists())
        self.assertEqual(self.secret.id, 1)
        self.assertEqual(self.secret.user_id, self.user.id)
        self.assertEqual(self.secret.description, self.user.id)

