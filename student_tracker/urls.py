
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('issue/', include('issue.urls')),
    path('support/', include('support.urls')),
    path('admin/', admin.site.urls),
]
