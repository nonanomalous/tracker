from django.contrib.auth.models import Group
from rest_framework import serializers

from account.models import User
from issue.models import Comment, Document, Issue, Link, Progress, Reason, Status


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'message',
            'progress',
            'link',
            'document',
        ]

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'file',
        ]

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            'anchortext',
            'summary',
        ]