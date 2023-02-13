from rest_framework import serializers
from issue.models import Comment, Document, Link, Progress, Reason

class ProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = [
            'assignee',
            'team',
            'issue',
            'reason',
            'description',
        ]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'url',
            'message',
            'progress',
            'link',
            'document',
        ]

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = [
            'url',
            'file',
        ]

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = [
            'url',
            'anchortext',
            'summary',
        ]