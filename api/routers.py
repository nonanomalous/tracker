from rest_framework import routers

from .views import IssueViewSet, UserViewSet, GroupViewSet, DocumentViewSet, LinkViewSet, CategoryViewSet, SubCategoryViewSet, StatusViewSet, ReasonViewSet, ProgressViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'issues', IssueViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'links', LinkViewSet)
router.register(r'categorys', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'reasons', ReasonViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'comments', CommentViewSet)
