
from rest_framework import serializers
from issue.models import Status

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['url',
                 'name',
                 ]