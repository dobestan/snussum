from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User


class APIMessageBaseTest(APITestCase):
    def setUp(self):
        self.username = "test_username"
        self.password = "test_password"
        self.user = User.objects.create_user(username=self.username, password=self.password)


class APIMessageMixin(object):
    def test_login_required(self):
        data = {}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.login(username=self.username, password=self.password)
        self.assertTrue(response)

        response = self.client.put(self.url, data, format="json")
        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class APIMessageSMSTest(APIMessageBaseTest, APIMessageMixin):
    def setUp(self):
        super(APIMessageSMSTest, self).setUp()
        self.url = reverse("api:sms")

    def test_send_sms(self):
        self.client.login(username=self.username, password=self.password)
        data = {
            'to': "010-2220-5736",
            'body': self.__class__.__name__,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIMessageEmailTest(APIMessageBaseTest, APIMessageMixin):
    def setUp(self):
        super(APIMessageEmailTest, self).setUp()
        self.url = reverse("api:email")

    def test_send_email(self):
        self.client.login(username=self.username, password=self.password)
        data = {
            'to': "dobestan@gmail.com",
            'subject': self.__class__.__name__,
            'body': self.__class__.__name__,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
