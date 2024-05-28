from django.test import TestCase,Client
from django.urls import reverse
from chat.models import Room
from accounts.models import CustomUser

class BaseTest(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='test_user1', password='test_password',email='user1@user1.com')
        self.user2 = CustomUser.objects.create_user(username='test_user2', password='test_password',email='user2@user2.com')
        
    def test_room_to_string(self):
        room = Room.objects.create(user1=self.user1, user2=self.user2)
        self.assertEqual(str(room), f'{self.user1.username} - {self.user2.username}')
    
    def test_url_resolves_to_room_view_and_has_right_context(self):
        self.client.login(username='test_user1', password='test_password')
        response = self.client.get(reverse('private_room',kwargs={'to_user':self.user2.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/private_room.html')
        self.assertEqual(response.context['to_user'], self.user2.username)
        self.assertEqual(response.context['username'], self.user1.username)
        
    def test_index_view_sends_all_users_and_user_has_to_be_logged_in(self):
        self.client.login(username='test_user1', password='test_password')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/index.html')
        self.assertEqual(len(response.context['users']), 2)
        

        
        