from django.test import TestCase
from django.urls import reverse
from accounts.views import SignUpView
from accounts.models import CustomUser

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.user = {
            'email': 'test@test.com',
            'username': 'test',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

        self.superuser = {
            'email': 'superuser@superuser.com',
            'username': 'superuser',
            'password': 'superuserpassword',
        }

        return super().setUp()
    
    def test_register_view(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
    
    def test_valueError_when_user_has_no_email(self):
        self.user['email'] = ''
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(response.context['form'].errors['email'], ['This field is required.'])

    def test_valueError_when_user_email_is_already_in_use(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertEqual(response.context['form'].errors['email'], ['This email is already in use.'])

    def test_createsuperuser(self):
        result = CustomUser.objects.create_superuser(**self.superuser)
        self.assertTrue(result.is_superuser)
        self.assertTrue(result.is_staff)
        self.assertTrue(result.is_active)

    def test_model_user_str(self):
        response=self.client.post(self.register_url, self.user, format='text/html')
        user = CustomUser.objects.get(username=self.user['username'])
        self.assertEqual(str(user), user.username)
        
        
        
        
        
        

