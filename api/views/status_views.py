from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response

from api.permissions import IsAdminOrReadOnly
from api.serializers import ReasonSerializer, StatusSerializer
from issue.models import Reason, Status


class ReasonList(generics.ListCreateAPIView):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
    permission_classes = [IsAdminOrReadOnly]

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminOrReadOnly]