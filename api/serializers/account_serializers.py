from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # issues = serializers.PrimaryKeyRelatedField(many=True, queryset=Issue.objects.all())

    class Meta:
        model = User
        fields = ['name', 'email', 'groups', 'issues']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['name', 'user_set']
