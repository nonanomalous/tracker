from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_root),
    path('issues/', views.IssueList.as_view(), name='issue-list'),
    path('issue/<int:pk>/', views.IssueDetail.as_view(), name='issue-detail'),
    path('issue/<int:issue_pk>/progress/', views.ProgressList.as_view(), name='progress-list'),
    path('progress/<int:pk>/', views.ProgressDetail.as_view(), name='progress-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('groups/', views.GroupList.as_view(), name='group-list'),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),
    path('documents/', views.DocumentList.as_view(), name='document-list'),
    path('document/<int:pk>/', views.DocumentDetail.as_view(), name='document-detail'),
    path('links/', views.LinkList.as_view(), name='link-list'),
    path('link/<int:pk>/', views.LinkDetail.as_view(), name='link-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/', views.SubCategoryList.as_view(), name='subcategory-list'),
    path('subcategory/<int:pk>/', views.SubCategoryDetail.as_view(), name='subcategory-detail'),
    path('reasons/', views.ReasonList.as_view(), name='reason-list'),
    path('reason/<int:pk>/', views.ReasonDetail.as_view(), name='reason-detail'),
    path('status/', views.StatusList.as_view(), name='status-list'),
    path('status/<int:pk>/', views.StatusDetail.as_view(), name='status-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)