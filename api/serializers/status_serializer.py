
from rest_framework import serializers
from issue.models import Reason, Status

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['url',
                 'name',
                 ]

class ReasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reason
        fields = ['url',
                 'name',
                 ]