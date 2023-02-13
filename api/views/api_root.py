from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'issues': reverse('issue-list', request=request, format=format),
        'progress': reverse('progress-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'documents': reverse('document-list', request=request, format=format),
        'links': reverse('link-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'subcategories': reverse('subcategory-list', request=request, format=format),
        'statuses': reverse('status-list', request=request, format=format),
        'reasons': reverse('reason-list', request=request, format=format),
    })