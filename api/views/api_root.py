from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'issues': reverse('api:issue-list', request=request, format=format),
        'progress': reverse('api:progress-list', kwargs={'issue_pk':3}, request=request, format=format),
        'comments': reverse('api:comment-list', request=request, format=format),
        'users': reverse('api:user-list', request=request, format=format),
        'groups': reverse('api:group-list', request=request, format=format),
        'documents': reverse('api:document-list', request=request, format=format),
        'links': reverse('api:link-list', request=request, format=format),
        'categories': reverse('api:category-list', request=request, format=format),
        'subcategories': reverse('api:subcategory-list', request=request, format=format),
        'statuses': reverse('api:status-list', request=request, format=format),
        'reasons': reverse('api:reason-list', request=request, format=format),
    })