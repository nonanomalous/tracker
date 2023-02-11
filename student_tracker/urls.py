
from django.contrib import admin
from django.urls import path, include

from api.routers import router as apirouter

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(apirouter.urls)),
    # path('issue/', include('issue.urls')),
    path('support/', include('support.urls')),
    path('admin/', admin.site.urls),
]
