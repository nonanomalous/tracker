from django.db import models


class OpenIssueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status__name="Closed").order_by('pk')

class ClosedIssueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__name="Closed").order_by('pk')

class DeletedIssueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__name="Deleted").order_by('pk')