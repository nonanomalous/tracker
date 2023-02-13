from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response

from api.permissions import IsAdminOrReadOnly
from api.serializers import StatusSerializer
from issue.models import Status


class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]

class StatusDetail(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]