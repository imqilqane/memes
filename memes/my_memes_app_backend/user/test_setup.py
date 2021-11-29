from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.regiter_url = reverse('user:register')
        self.login_url = reverse('user:login')
        self.request_new_pass_url = reverse('user:request_new')

        self.user_data = {
            'email': 'email@gmail.com',
            'username': 'myusername',
            'password': 'password'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
