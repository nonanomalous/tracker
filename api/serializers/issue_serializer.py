
from rest_framework import serializers
from issue.models import Issue

class IssueSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.ReadOnlyField(source='student.id')
    subcategory = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    status = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Issue
        fields = ['id',
                 'brief',
                 'description',
                 'student',
                 'subcategory',
                 'status',
                 ]
        optional_fields = []

