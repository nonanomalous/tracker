from django.test import TestCase, Client
from django.urls import reverse
from account.models import User
from issue.models import Issue

class TestIssueListView(TestCase):
    fixtures = ['initial_data.json']
    def setUp(self):
        self.client = Client()
        self.url = reverse('issue:home')

        self.student_username = 'student@example.com'
        self.student_password = 'uol'
        self.student2_username = 'student2@example.com'
        self.student2_password = 'uol'
        self.support_username = 'level1@example.com'
        self.support_password = 'uol'

        self.student_user = User.objects.get(email=self.student_username)
        self.support_user = User.objects.get(email=self.support_username)
        
        self.student_issues_list = Issue.openIssues.filter(student=self.student_user).order_by('pk')
        self.support_issues_list = Issue.openIssues.all().order_by('pk')

    def test_correct_template_used(self):
        self.client.login(username=self.student_username, password=self.student_password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issue/issue_list.html')
        
    def test_issue_list_view_with_student_login(self):
        self.client.login(username=self.student_username, password=self.student_password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        items_list_from_response = response.context_data['issue_list']
        self.assertQuerysetEqual(items_list_from_response, self.student_issues_list)

    def test_issue_list_view_with_support_login(self):
        self.client.login(username=self.support_username, password=self.support_password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        items_list_from_response = response.context_data['issue_list']
        self.assertQuerysetEqual(items_list_from_response, self.support_issues_list)

    