from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('document', DocumentCreateView.as_view(), name='document-create'),
]
