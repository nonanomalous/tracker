
from rest_framework import serializers
from issue.models import SubCategory, Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
                  'name',
                  'category',
                  'supportedBy',
                  'category',
                  'links',
                  'documents',
                  ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
                  'name',
                  'subcategories',
                  ]
