from django.db import models


class OpenIssueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status__name="Closed")

class ClosedIssueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status__name="Closed")