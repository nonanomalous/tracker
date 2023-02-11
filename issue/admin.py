from django.contrib import admin
from .models import Document, Link, Category, SubCategory, Status, Issue, Reason, Progress, Comment

class DocumentAdmin(admin.ModelAdmin): pass
class LinkAdmin(admin.ModelAdmin): pass
class CategoryAdmin(admin.ModelAdmin): pass
class SubCategoryAdmin(admin.ModelAdmin): pass
class StatusAdmin(admin.ModelAdmin): pass
class IssueAdmin(admin.ModelAdmin): pass
class ReasonAdmin(admin.ModelAdmin): pass
class ProgressAdmin(admin.ModelAdmin): pass
class CommentAdmin(admin.ModelAdmin): pass

admin.site.register(Document,DocumentAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Issue,IssueAdmin)
admin.site.register(Reason,ReasonAdmin)
admin.site.register(Progress,ProgressAdmin)
admin.site.register(Comment,CommentAdmin)