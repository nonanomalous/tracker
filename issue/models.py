from django.db import models
from django.contrib.auth.models import Group
from account.models import User

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

class Category(models.Model):
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['id']

class SubCategory(models.Model):
    def default_supported_by():
        group, _ = Group.objects.get_or_create(name="Level1")
        return group

    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supportedBy = models.ForeignKey(Group, null=True, blank=True, default=default_supported_by, on_delete=models.SET_NULL)
    links = models.ManyToManyField(Link)
    documents = models.ManyToManyField(Document)

    def __str__(self):
        return f'{self.category.name} - {self.name}'

    class Meta:
        verbose_name_plural = "SubCategories"
        ordering = ['id']

class Status(models.Model):
    name = models.CharField(max_length=32, default="")

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ['id']

class Issue(models.Model):
    def default_status():
        status, _ = Status.objects.get_or_create(name="New")
        return status
    def default_subcategory():
        category, _ = Category.objects.get_or_create(name="General")
        subcategory, _ = SubCategory.objects.get_or_create(name="General", category=category)
        return subcategory

    brief = models.CharField(max_length=32, default="")
    description = models.CharField(max_length=255, default="")
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, default=default_subcategory, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, default=default_status, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.student.name} - {self.brief}'

class Reason(models.Model):
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return f'{self.name}'
    
class Progress(models.Model):
    assignee = models.ForeignKey(User, related_name="assigned_tickets", on_delete=models.CASCADE)
    team = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)
    issue = models.ForeignKey(Issue,on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    closedby = models.ForeignKey(User, related_name="tickets_closed", null=True, on_delete=models.SET_NULL)
    finishedDate = models.DateTimeField()
    
    def __str__(self):
        return f'Issue {self.issue.id} | pid: {self.id} | {self.reason.name}'
    
    class Meta:
        verbose_name_plural = "Progress"
        ordering = ['issue']


class Comment(models.Model):
    message = models.TextField(blank=True, null=True)
    progress = models.ForeignKey(Progress,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    link = models.ManyToManyField(Link)
    document = models.ManyToManyField(Document)

    def __str__(self):
        return f'Issue {self.progress.issue.id}: {self.reason.name}'