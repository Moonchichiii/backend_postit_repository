from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTests(APITestCase):

    def test_registration(self):
        url = reverse('users:user-registration')
        data = {
            'username': 'TestUser24211', 
            'email': 'TestUser22241@gmail.com', 
            'password': 'TestUser', 
            'confirm_password': 'TestUser'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):        
        User.objects.create_user(username='TestUser24211', email='TestUser22241@gmail.com', password='TestUser')
        url = reverse('users:token_obtain_with_user_id')
        data = {'username': 'TestUser24211', 'password': 'TestUser'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)