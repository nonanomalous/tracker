from rest_framework import generics, status
from rest_framework.response import Response

from api.permissions import IsReportingStudentOrStaff
from api.serializers import IssueSerializer
from issue.models import Issue, Progress


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsReportingStudentOrStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        newProgress = Progress.objects.create(issue=serializer.instance,
            description="Hello, your ticket is pending assignment to an agent.")
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """ 
        If user doesn't have non-Student role, filter list
        to show only tickets reported by themselves
        """
        queryset = Issue.objects.exclude(status__name="Closed").prefetch_related("progress")
        if not self.request.user.groups.exclude(name='Student').exists():
            queryset = queryset.filter(student=self.request.user).prefetch_related("progress")
        return queryset
    
    def perform_create(self, serializer):
        """ 
        Default "reported by" to logged in user for new issues
        and create first progress reason "created"
        """
        serializer.save(student=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = IssueSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class IssueDetail(generics.RetrieveUpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsReportingStudentOrStaff]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)