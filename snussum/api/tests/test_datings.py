from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from relationships.models.dating import Dating


class DatingCommentTest(APITestCase):
    def setUp(self):
        self.boy_username = "boyuser"
        self.boy_password = "boypassword"
        self.boy = User.objects.create_user(username=self.boy_username, password=self.boy_password)

        self.girl_username = "girluser"
        self.girl_password = "girlpassword"
        self.girl = User.objects.create_user(username=self.girl_username, password=self.girl_password)

        self.dating = Dating.objects.create(boy=self.boy, girl=self.girl)

        self.url = reverse("api:dating-comment", kwargs={'hash_id': self.dating.hash_id})

        self.other_user_username = "otheruser"
        self.other_user_password = "otherpassword"
        self.other_user = User.objects.create_user(username=self.other_user_username, password=self.other_user_password)


    def test_login_required(self):
        data = {}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.login(username=self.other_user_username, password=self.other_user_password)
        self.assertTrue(response)

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.logout()
        response = self.client.login(username=self.boy_username, password=self.boy_password)
        self.assertTrue(response)

        response = self.client.post(self.url, data, format="json")
        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)
