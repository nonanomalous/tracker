from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from issue.models import Issue

from .data_user import *
from .data_issues import ISSUES, PROGRESS
from issue import load

User = get_user_model()

class ProgressAddTests(APITestCase):   
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
    
    def test_add_progress_to_issue(self):
        """
        A support user should be able to move ahead progress on an issue
        """
        user = User.objects.get(email=TEST_L1_USER)
        self.client.force_authenticate(user)
        response = self.client.get(reverse('api:issue-list'))
        data = response.json()
        issue_id = data[0]['id']
        
        progress = PROGRESS['PROGRESS1']
        progress['issue'] = issue_id
        progress['assignee'] = user.id
        self.client.post(reverse('api:progress-list'), progress, format='json')


        self.client.logout()