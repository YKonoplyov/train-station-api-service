from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class UserAppTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        url = reverse("user:create")
        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)

    def test_user_profile_retrie(self):
        user = get_user_model().objects.create_user(
            email="test@example.com", password="testpassword"
        )

        self.client.force_authenticate(user=user)

        url = reverse("user:manage-user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], user.email)

    def test_user_profile_update(self):
        user = get_user_model().objects.create_user(
            email="test@example.com", password="testpassword"
        )

        self.client.force_authenticate(user=user)

        url = reverse("user:manage-user")
        data = {"email": "updated@example.com"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], data["email"])

        user.refresh_from_db()

        self.assertEqual(user.email, data["email"])
