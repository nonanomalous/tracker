from django.test import TestCase, Client
from django.urls import reverse
from account.models import User
from issue.models import Issue

from bs4 import BeautifulSoup

class TestIssueListView(TestCase):
    fixtures = ['initial_data.json']
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('issue:updateIssue', kwargs={'pk':5})

        self.student_username = 'student@example.com'
        self.student_password = 'uol'
        self.student2_username = 'student2@example.com'
        self.student2_password = 'uol'
        self.support_username = 'level1@example.com'
        self.support_password = 'uol'

        self.student_user = User.objects.get(email=self.student_username)       # issues 1-4
        self.student2_user = User.objects.get(email=self.student2_username)     # issues 5-8
        self.support_user = User.objects.get(email=self.support_username)

    def test_correct_template_used(self):
        """ ensure we get the issue_detail template """
        self.client.login(username=self.student2_username, password=self.student2_password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issue/issue_update.html')
        
    def test_issue_detail_student_cannot_see_others_tickets(self):
        """ Login as student 2 should not see ticket 1, should see ticket 5"""
        self.client.login(username=self.student2_username, password=self.student2_password)
        response = self.client.get(reverse('issue:updateIssue', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 403)
        ### wrong user was forbidden ###
        self.client.logout()
        self.client.login(username=self.student2_username, password=self.student2_password)
        response = self.client.get(reverse('issue:updateIssue', kwargs={'pk':5}))
        self.assertEqual(response.status_code, 200)
        ### correct user was accepted ###
        self.client.logout()
        

    def test_issue_detail_student_cannot_escalate_agent_can(self):
        self.client.login(username=self.support_username, password=self.support_password)
        getResponse = self.client.get(reverse('issue:updateIssue', kwargs={'pk':2}))
        soup = BeautifulSoup(getResponse.rendered_content, features="html.parser")
        form = {element['name']: element['value'] for element in soup.find_all('input')}
        form.update({element['name']: element.text.strip() for element in soup.find_all('textarea')})
        form['subcategory'] = soup.find_all('option', {'selected':True})[0]['value']
        form['Escalate'] = ''
        postResponse = self.client.post(reverse('issue:updateIssue', kwargs={'pk':2}),data=form, follow=True)
        self.assertEqual(postResponse.status_code, 200) 
        ### agent succeeded in escalating ticket ###
        
        self.client.logout()
        self.client.login(username=self.student_user, password=self.student_password)
        soup = BeautifulSoup(getResponse.rendered_content, features="html.parser")
        form = {element['name']: element['value'] for element in soup.find_all('input')}
        form.update({element['name']: element.text.strip() for element in soup.find_all('textarea')})
        form['subcategory'] = soup.find_all('option', {'selected':True})[0]['value']
        form['Escalate'] = ''
        postResponse = self.client.post(reverse('issue:updateIssue', kwargs={'pk':2}),data=form, follow=True)
        self.assertEqual(postResponse.status_code, 403) 
        ### student failed to escalate ticket ###
        