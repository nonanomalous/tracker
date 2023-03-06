from django.db import models
from django.contrib.auth.models import Group, GroupManager
from account.models import User
from .managers import OpenIssueManager, ClosedIssueManager
from .mixins import GetterMixin

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    def __str__(self):
        return f'{self.file.name}'

class Link(models.Model):
    url = models.SlugField(max_length=255)
    anchortext = models.CharField(max_length=32)
    summary = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.anchortext}'

class Category(models.Model, GetterMixin):
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['id']

class MyGroup(Group, GetterMixin):
    objects = GroupManager()
    class Meta:
        proxy = True

class SubCategory(models.Model, GetterMixin):
    def default_supported_by():
        group, _ = Group.objects.get_or_create(name="Level1")
        return group.id
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, related_name='subcategories', default=Category.GeneralId, on_delete=models.SET_DEFAULT)
    supportedBy = models.ForeignKey(Group, related_name='support_categories', default=1, on_delete=models.SET_DEFAULT)
    links = models.ManyToManyField(Link, blank=True)
    documents = models.ManyToManyField(Document, blank=True)

    def __str__(self):
        return f'{self.category.name} - {self.name}'

    class Meta:
        verbose_name_plural = "SubCategories"
        ordering = ['id']

class Status(models.Model, GetterMixin):
    name = models.CharField(max_length=32, default="New")
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ['id']

class Issue(models.Model):
    def default_status():
        status, _ = Status.objects.get_or_create(name="New")
        return status.id
    def default_subcategory():
        category, _ = Category.objects.get_or_create(name="General")
        subcategory, _ = SubCategory.objects.get_or_create(name="General", category=category)
        return subcategory.id
    brief = models.CharField(max_length=128, default="")
    description = models.TextField(default="")
    student = models.ForeignKey(User, related_name='issues', on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, default=SubCategory.GeneralId, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, default=Status.NewId, on_delete=models.PROTECT)
    escalation = models.ForeignKey(Group, default=1, on_delete=models.SET_DEFAULT)

    objects = models.Manager()
    openIssues = OpenIssueManager()
    closedIssues = ClosedIssueManager()

    def __str__(self):
        return f'{self.student.name} - {self.brief}'
    
    def get_current_progress(self):
        return self.progress.filter(active=1).last()

    def get_current_subcategory(self):
        currentProgress = self.get_current_progress()
        if currentProgress and currentProgress.team:
            return currentProgress.team.name
        else: return None
    
    def get_current_team(self):
        currentProgress = self.get_current_progress()
        if currentProgress and currentProgress.team:
            return currentProgress.team.name
        else: return None
    
    def get_current_assignee(self):
        currentProgress = self.get_current_progress()
        if currentProgress and currentProgress.assignee:
            return currentProgress.assignee.name
        else: return None
    
    def get_current_due(self):
        if currentProgress := self.get_current_progress():
            return currentProgress.due

class Reason(models.Model, GetterMixin):
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return f'{self.name}'
    
class Progress(models.Model):
    assignee = models.ForeignKey(User, null=True, blank=True, default=None, related_name="assigned_tickets", on_delete=models.CASCADE)
    team = models.ForeignKey(Group, default=MyGroup.GeneralId, on_delete=models.SET_DEFAULT)
    issue = models.ForeignKey(Issue, related_name='progress', on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, null=True, default=Reason.CreatedId, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    due = models.DateTimeField(null=True, blank=True)
    closedby = models.ForeignKey(User, related_name="tickets_closed", null=True, blank=True, on_delete=models.SET_NULL)
    finishedDate = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'Issue {self.issue.id} | pid: {self.id} | {self.reason.name}'
    
    class Meta:
        verbose_name_plural = "Progress"
        ordering = ['issue']


class Comment(models.Model):
    message = models.TextField(blank=True, null=True)
    progress = models.ForeignKey(Progress, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    link = models.ManyToManyField(Link, blank=True)
    document = models.ManyToManyField(Document, blank=True)

    def __str__(self):
        return f'Issue {self.progress.issue.id}: {self.reason.name}'