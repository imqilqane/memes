from .test_setup import TestSetUp
from .models import User
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


class TestViews(TestSetUp):

    def test_user_regestration_with_blank_input(self):
        """test the case when user try to register with blank data"""

        res = self.client.post(self.regiter_url)
        self.assertEqual(res.status_code, 400)

    def test_user_regestration_with_valid_data(self):
        """test the case when user try to register with valid data"""

        res = self.client.post(self.regiter_url, self.user_data, format='json')
        self.assertEqual(res.status_code, 201)
        return res

    def test_user_verifien_his_account_popry(self):
        """test the case when the user want to virify his propre account"""
        registered_user = self.test_user_regestration_with_valid_data()

        relative_link = reverse("user:verify")
        absulot_verifing_link = f"{relative_link}?token={registered_user.data['token']}"
        res = self.client.get(absulot_verifing_link)
        self.assertEqual(res.status_code, 200)

    def test_user_login_with_inverified_account(self):
        """test the case when a user try to log in but didnt verify his account"""

        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 401)

    def test_user_login_with_verified_account(self):
        """test the case when a user try to log with verified account"""

        registerd_user_data = self.client.post(
            self.regiter_url, self.user_data, format='json')
        user = User.objects.get(email=registerd_user_data.data['email'])
        user.is_verify = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
