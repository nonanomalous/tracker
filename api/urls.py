from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('groups/', views.GroupList.as_view(), name='group-list'),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),
    path('issues/', views.IssueList.as_view(), name='issue-list'),
    path('issue/<int:pk>/', views.IssueDetail.as_view(), name='issue-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/', views.SubCategoryList.as_view(), name='subcategory-list'),
    path('subcategory/<int:pk>/', views.SubCategoryDetail.as_view(), name='subcategory-detail'),
    path('status/', views.StatusList.as_view(), name='status-list'),
    path('status/<int:pk>/', views.StatusDetail.as_view(), name='status-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)