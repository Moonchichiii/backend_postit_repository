from django.urls import reverse

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status



# Create your tests here.


class UserAccountTests(APITestCase):

    def setUp(self):
        # create test user
        self.user = User.objects.create_user(username='tester2024', password='tester2024')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_registration(self):
        """
        testing to verify user registration
        """
        data = {
            "username": "tester2025",
            "email": "tester2025@gmail.com",
            "password": "tester2025",
            "confirm_password": "tester2025"
        }
        response = self.client.post(reverse('users:user-registration'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        testing to verify user login
        """
        data = {
            "username": "tester2024",
            "password": "tester2024"
        }
        response = self.client.post(reverse('users:user-login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_logout(self):
        """
        Test to verify user logout
        """
        response = self.client.post(reverse('users:user-logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(user=self.user).exists())

    