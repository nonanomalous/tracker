
from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'issue'
urlpatterns = [
    path('', IssueListView.as_view(), name='home'),
    path('create/', IssueCreateView.as_view(), name='createIssue'),
    path('update/<int:pk>/', IssueUpdateView.as_view(), name='updateIssue'),
]
