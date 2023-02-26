from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from issue.models import Issue

from .data_user import *
from .data_issues import ISSUES
from issue import load


User = get_user_model()

class IssueCreateTests(APITestCase):
    def setUp(self):
        load.run()
    
    def tearDown(self): pass
    
    def test_add_issue_user1(self):
        """
        Login and create issue, make sure the first 
        in user is the issue's "reported by" student
        """
        user = User.objects.get(email=TEST_USER_1)
        self.client.force_authenticate(user)
        response = self.client.post(reverse('api:issue-list'), ISSUES['ISSUE1'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Issue.objects.filter(student__id=user.id).first().brief, ISSUES['ISSUE1']['brief'])
        self.client.logout()

    def test_add_issue_user2(self):
        """
        Login and create issue, make sure the second 
        user's id is the issue's "reported by" student
        """
        user = User.objects.get(email=TEST_USER_2)
        self.client.force_authenticate(user)
        response = self.client.post(reverse('api:issue-list'), ISSUES['ISSUE1'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Issue.objects.filter(student__id=user.id).first().brief, ISSUES['ISSUE1']['brief'])
        self.client.logout()

class IssuesListTests(APITestCase):   
    def setUp(self):
        load.run()
        user1 = User.objects.get(email=TEST_USER_1)
        self.client.force_authenticate(user1)
        self.client.post(reverse('api:issue-list'), ISSUES['ISSUE1'], format='json')
        self.client.logout()
        user2 = User.objects.get(email=TEST_USER_2)
        self.client.force_authenticate(user2)
        self.client.post(reverse('api:issue-list'), ISSUES['ISSUE2'], format='json')
        self.client.logout()

    def test_user1_list_issues_is_filtered(self):
        """
        When user1 gets a list of all issues they should
        only see issues created by themselves
        """
        user = User.objects.get(email=TEST_USER_1)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('api:issue-list'))
        for data in response.json():
            self.assertEqual(data['student'], user.id)
        self.client.logout()

    def test_user2_list_issues_is_filtered(self):
        """
        When user2 gets a list of all issues they should
        only see issues created by themselves
        """
        user = User.objects.get(email=TEST_USER_2)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('api:issue-list'))
        for data in response.json():
            self.assertEqual(data['student'], user.id)
        self.client.logout()

    def test_support_list_issues_shows_all(self):
        """
        A support user should see issues created by all students
        """
        user1 = User.objects.get(email=TEST_USER_1)
        user2 = User.objects.get(email=TEST_USER_2)
        l1_user = User.objects.get(email=TEST_L1_USER)
        self.client.force_authenticate(l1_user)
        response = self.client.get(reverse('api:issue-list'))
        data = response.json()
        self.assertEqual(data[0]['student'], user1.id)
        self.assertEqual(data[1]['student'], user2.id)
        self.client.logout()

