
from rest_framework import serializers
from issue.models import Issue

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.ReadOnlyField(source='student.username')
    status = serializers.ReadOnlyField(source='status.name')

    class Meta:
        model = Issue
        fields = ['url',
                 'student',
                 'brief',
                 'description',
                 'subcategory',
                 'status',
                 'progress',
                 ]
        optional_fields = []