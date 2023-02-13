
from rest_framework import serializers
from issue.models import SubCategory, Category


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['url',
                  'id',
                  'name',
                  'category',
                  'supportedBy',
                  'category',
                  'links',
                  'documents',
                  ]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url',
                  'id',
                  'name',
                  'subcategories',
                  ]
