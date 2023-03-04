
from rest_framework import serializers
from issue.models import Reason, Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
                 'name',
                 ]

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = [
                 'name',
                 ]