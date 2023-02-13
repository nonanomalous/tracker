from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

from issue.models import Issue

User=get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'name', 'email', 'groups', 'issues']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'id', 'name', 'user_set']
