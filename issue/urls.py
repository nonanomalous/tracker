
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', IssueListView.as_view(), name='issue-list'),
]
