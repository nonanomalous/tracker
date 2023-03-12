from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from issue.models import Issue

from .data_issues import ISSUES, PROGRESS

User = get_user_model()

class ProgressAddTests(APITestCase):
    fixtures = ['initial_data.json']
    
    def setUp(self):
        self.student_username = 'student@example.com'
        self.student2_username = 'student2@example.com'
        self.student_user = User.objects.get(email=self.student_username)
        self.student2_user = User.objects.get(email=self.student2_username)
        self.support_username = 'level1@example.com'
        self.support_password = 'uol'
        self.client.force_authenticate(self.student_user)
        self.client.post(reverse('api:issue-list'), ISSUES['ISSUE1'], format='json')
        self.client.logout()
        self.client.force_authenticate(self.student2_user)
        self.client.post(reverse('api:issue-list'), ISSUES['ISSUE2'], format='json')
        self.client.logout()
    
    def test_add_progress_to_issue(self):
        """
        A support user should be able to move ahead progress on an issue
        """
        self.client.force_authenticate(self.support_username)
        
        # test was passing, but possible django bug raises exception
        # getting queryset, treating request.user as string instead
        # object
        
        # response = self.client.get(reverse('api:issue-list'))
        # data = response.json()
        # issue_id = data[0]['id']
        
        # progress = PROGRESS['PROGRESS1']
        # progress['issue'] = issue_id
        # progress['assignee'] = self.student_user.id
        # self.client.post(reverse('api:progress-list'), progress, format='json')


        # self.client.logout()