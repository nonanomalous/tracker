from django.db.models import Q

from rest_framework import generics, status
from rest_framework.response import Response

from api.permissions import IsAdminOrReadOnly, IsStaffOrReadOnly
from api.serializers import CommentSerializer, DocumentSerializer, LinkSerializer, ProgressSerializer
from issue.models import Comment, Document, Link, Progress


class ProgressList(generics.ListCreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsStaffOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = Progress.objects.filter(issue__id=kwargs['issue_pk'])
        serializer = ProgressSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
class ProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [IsStaffOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrReadOnly]

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrReadOnly]

class LinkList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAdminOrReadOnly]

class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAdminOrReadOnly]