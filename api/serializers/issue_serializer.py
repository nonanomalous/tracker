from django.contrib.auth.models import Group
from django.urls import reverse

from rest_framework import serializers
from account.models import User
from issue.models import Issue, Progress, Reason, Status, SubCategory

from datetime import datetime


class ProgressHyperLink(serializers.HyperlinkedModelSerializer):
    view_name = 'api:progress-detail'
    queryset = Issue.objects.all()

    def get_url(self, obj, view_name, request, format):
        view_name = 'api:issue-detail'
        url_kwargs = {
            # 'issue_pk': obj.issue.pk,
            'pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
        #    'issue__pk': view_kwargs['issue_pk'],
           'pk': view_kwargs['pk']
        }
        return self.get_queryset().get(**lookup_kwargs)

class ProgressSerializer(ProgressHyperLink):
    assignee = serializers.PrimaryKeyRelatedField(
        many=False, queryset=User.staff.all(), read_only=False)
    team = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Group.objects.exclude(name="Student"), read_only=False)
    issue = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Issue.objects.all(), read_only=False)
    reason = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Reason.objects.all(), read_only=False)

    class Meta:
        model = Progress
        fields = [
            'id',
            'url',
            'assignee',
            'team',
            'issue',
            'reason',
            'description',
        ]
        extra_kwargs = {'url': {'view_name': 'api:progress-detail'}}

    def create(self, validated_data):
        user = validated_data.pop('user')
        if validated_data['reason'] == Reason.objects.get(name='Resolved'):
            issue = validated_data['issue']
            issue.status = Status.objects.get(name='Closed')
            issue.closedby = user
            issue.save()
            validated_data['finishedDate'] = datetime.now()
        return Progress.objects.create(**validated_data)

class BasicProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = [
            'id',
            'team',
            'reason',
        ]

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.ReadOnlyField(source='student.id')
    subcategory = serializers.PrimaryKeyRelatedField(
        many=False, queryset=SubCategory.objects.all(), read_only=False)
    status = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    progress = BasicProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = [
            'id',
            'url',
            'brief',
            'description',
            'student',
            'subcategory',
            'status',
            'progress'
        ]
        extra_kwargs = {'url': {'view_name': 'api:issue-detail'}}
        optional_fields = []

