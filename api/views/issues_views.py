from rest_framework import generics
from rest_framework.response import Response

from api.permissions import IsReportingStudentOrStaff
from api.serializers import IssueSerializer
from issue.models import Issue


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsReportingStudentOrStaff]

    def get_queryset(self):
        queryset = Issue.objects.exclude(status__name="Closed")
        if self.request.user.groups.filter(name='Student').exists():
            queryset = queryset.filter(student=self.request.user)
        return queryset
        
    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IssueSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class IssueDetail(generics.RetrieveUpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsReportingStudentOrStaff]