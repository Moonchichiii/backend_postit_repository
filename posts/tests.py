from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


# Create your tests here.


class PostViewSetTestCase(APITestCase):
           
    def test_get_post(self):
        """
        get a post
        """
        url = '/posts/'
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
