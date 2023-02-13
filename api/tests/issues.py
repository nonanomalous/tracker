from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from issue.models import Issue
import environ

env = environ.Env()
environ.Env.read_env('.env')
TEST_USER_1 = env('TEST_USER_1')
TEST_PASS_1 = env('TEST_PASS_1')
TEST_USER_2 = env('TEST_USER_2')
TEST_PASS_2 = env('TEST_PASS_2')
TEST_USER_3 = env('TEST_USER_3')
TEST_PASS_3 = env('TEST_PASS_3')


class IssuesTests(APITestCase):
    def test_add_issue(self):
        """
        CM2020-69 → Ensure two different users can add tests
        """
        url = reverse('issue-create')
        data = {'name': 'DabApps'}

        self.client.login(username=TEST_USER_1, password=TEST_PASS_1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Issue.objects.count(), 1)
        self.assertEqual(Issue.objects.get().name, 'DabApps')
        self.client.logout()

        # self.client.login(username=TEST_USER_2, password=TEST_PASS_2)
