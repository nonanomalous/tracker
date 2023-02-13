from rest_framework import serializers
from account.models import User
from django.contrib.auth.models import Group

from issue.models import Issue, Document, Link, Category, SubCategory, Status, Reason, Progress, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = User
            fields = ['url', 'username', 'name', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['url', 'file']

class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['url','anchortext','summary',]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['url', 'name', 'category', ]

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['url', 'name']

class ReasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reason
        fields = ['url', 'name']

class ProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = ['url', ]

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'message', 'progress', 'link', 'document']