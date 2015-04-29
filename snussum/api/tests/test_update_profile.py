from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from users.models.university import University


class APIUpdateUniversityTest(APITestCase):

    def setUp(self):
        # Create a user for testing
        self.username = "test_username"
        self.password = "test_password"

        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.url = reverse("api:update-university")

        self.university = University.objects.create(
            full_name="fullname",
            short_name="short",
            email="snu.ac.kr",
            slug="SNU",
        )

    def test_login_required(self):
        data = {}
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.login(username=self.username, password=self.password)
        self.assertTrue(response)

        response = self.client.put(self.url, data, format="json")
        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_university_with_invalid_data(self):
        self.client.login(username=self.username, password=self.password)
        data = {}
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_university(self):
        self.client.login(username=self.username, password=self.password)

        data = {
            'username': self.username,
            'university': self.university.id,
        }
        response = self.client.put(self.url, data, format="json")
        self.user = User.objects.get(id=self.user.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.userprofile.university, self.university)
        self.assertEqual(
            self.user.email,
            self.username + "@" + self.university.email
        )


class APIUpdateNicknameTest(APITestCase):
    def setUp(self):
        # Create user for testing
        self.username = "test_username"
        self.password = "test_password"
        self.nickname = "test"
        self.user = User.objects.create_user(username=self.username, password=self.password)

        # Create user with nickname already taken
        self.user_already_taken_nickname_username = "test_username_taken"
        self.user_already_taken_nickname = User.objects.create_user(
            username=self.user_already_taken_nickname_username,
            password=self.password,
        )
        self.duplicate_nickname = "taken"
        self.user_already_taken_nickname.userprofile.nickname = self.duplicate_nickname
        self.user_already_taken_nickname.userprofile.save()

        self.url = reverse("api:update-nickname")
        self.client.login(username=self.username, password=self.password)

    def test_update_nickname(self):
        data = {'nickname': self.nickname}
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user = User.objects.get(id=self.user.id)
        self.assertEqual(self.user.userprofile.nickname, self.nickname)

    def test_update_nickname_already_taken(self):
        data = {'nickname': self.duplicate_nickname}
        response = self.client.put(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
