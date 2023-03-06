from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from account.views import logout_view, login_view
from issue.views import IssueListView

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', IssueListView.as_view(), name='home'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('issue/', include('issue.urls')),
    path('support/', include('support.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
