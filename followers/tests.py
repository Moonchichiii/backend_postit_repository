from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from .models import Follower
from profiles.models import Profile


# Create your tests here.

class FollowerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user('user1', 'user1@example.com', 'user1password')
        self.user2 = User.objects.create_user('user2', 'user2@example.com', 'user2password')
        self.user3 = User.objects.create_user('user3', 'user3@example.com', 'user3password') 

        
    def test_follow_multiple(self):
    
        self.client.force_authenticate(user=self.user1)
        response1 = self.client.post('/api/followers/', {'followed_profile': self.user2.profile.id})
        response2 = self.client.post('/api/followers/', {'followed_profile': self.user3.profile.id})

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 201)
        self.assertEqual(Follower.objects.count(), 2)

