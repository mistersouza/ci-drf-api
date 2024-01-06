from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

# Tests
class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='thiago', password='Cuiaba1983')

    def test_can_list_posts(self):
        thiago = User.objects.get(username='thiago')
        Post.objects.create(owner=thiago, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='thiago', password='Cuiaba1983')
        response = self.client.post('/posts/', {'title': 'testing title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_unauth_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'testing title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)