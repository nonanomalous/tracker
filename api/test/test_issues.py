from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from issue.models import Issue

from .data_issues import ISSUES


User = get_user_model()

class IssueCreateTests(APITestCase):
    fixtures = ["initial_data.json"]

    def setUp(self):
        self.student_username = 'student@example.com'
        self.student_password = 'uol'
        self.student2_username = 'student2@example.com'
        self.student_password = 'uol'
        self.support_username = 'level1@example.com'
        self.support_password = 'uol'
        self.student_user = User.objects.get(email=self.student_username)
        self.support_user = User.objects.get(email=self.support_username)
        self.student_issues_list = Issue.openIssues.filter(student=self.student_user).order_by('pk')
        self.support_issues_list = Issue.openIssues.all().order_by('pk')
    
    def test_add_issue_user1(self):
        """
        Login and create issue, make sure the first 
        in user is the issue's "reported by" student
        """
        user = User.objects.get(email=self.student_username)
        self.client.force_authenticate(user)
        data = ISSUES['ISSUE1']
        response = self.client.post(reverse('api:issue-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Issue.objects.filter(student__id=user.id).first().brief, ISSUES['ISSUE1']['brief'])
        self.client.logout()

    def test_add_issue_user2(self):
        """
        Login and create issue, make sure the second 
        user's id is the issue's "reported by" student
        """
        user = User.objects.get(email=self.student2_username)
        self.client.force_authenticate(user)
        response = self.client.post(reverse('api:issue-list'), ISSUES['ISSUE2'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Issue.objects.filter(student__id=user.id).first().brief, ISSUES['ISSUE2']['brief'])
        self.client.logout()

class IssuesListTests(APITestCase):
    fixtures = ["initial_data.json"]

    def setUp(self):
        self.student_username = 'student@example.com'
        self.student2_username = 'student2@example.com'
        self.support_username = 'level1@example.com'
        user1 = User.objects.get(email=self.student_username)
        self.client.force_authenticate(user1)
        self.client.post(reverse('api:issue-list'), ISSUES['ISSUE1'], format='json')
        self.client.logout()
        user2 = User.objects.get(email=self.student2_username)
        self.client.force_authenticate(user2)
        self.client.post(reverse('api:issue-list'), ISSUES['ISSUE2'], format='json')
        self.client.logout()

    def test_user1_list_issues_is_filtered(self):
        """
        When user1 gets a list of all issues they should
        only see issues created by themselves
        """
        user = User.objects.get(email=self.student_username)
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
        user = User.objects.get(email=self.student2_username)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('api:issue-list'))
        for data in response.json():
            self.assertEqual(data['student'], user.id)
        self.client.logout()

    def test_support_list_issues_shows_all(self):
        """
        A support user should see issues created by all students
        """
        user1 = User.objects.get(email=self.student_username)
        user2 = User.objects.get(email=self.student2_username)
        l1_user = User.objects.get(email=self.support_username)
        self.client.force_authenticate(l1_user)
        response = self.client.get(reverse('api:issue-list'))
        data = response.json()
        self.assertEqual(data[-2]['student'], user1.id)
        self.assertEqual(data[-1]['student'], user2.id)
        self.client.logout()

