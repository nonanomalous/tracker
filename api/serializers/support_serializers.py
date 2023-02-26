from django.contrib.auth.models import Group
from rest_framework import serializers

from account.models import User
from issue.models import Comment, Document, Issue, Link, Progress, Reason, Status

from datetime import datetime

class ProgressSerializer(serializers.ModelSerializer):
    assignee = serializers.PrimaryKeyRelatedField(many=False, queryset=User.staff.all(), read_only=False)
    team = serializers.PrimaryKeyRelatedField(many=False, queryset=Group.objects.exclude(name="Student"), read_only=False)
    issue = serializers.PrimaryKeyRelatedField(many=False, queryset=Issue.objects.all(), read_only=False)
    reason = serializers.PrimaryKeyRelatedField(many=False, queryset=Reason.objects.all(), read_only=False)

    class Meta:
        model = Progress
        fields = [
            'assignee',
            'team',
            'issue',
            'reason',
            'description',
        ]
    
    def create(self, validated_data):
        user = validated_data.pop('user')
        if validated_data['reason'] == Reason.objects.get(name='Resolved'):
            issue = validated_data['issue']
            issue.status = Status.objects.get(name='Closed')
            issue.closedby = user
            issue.save()
            validated_data['finishedDate'] = datetime.now()
        return Progress.objects.create(**validated_data)

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