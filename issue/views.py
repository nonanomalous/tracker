from django.shortcuts import render
from django.views.generic.list import ListView

from issue.models import Issue, Status

class IssueListView(ListView):
    model = Issue
    paginate_by = 50

    def get_queryset(self):

        return Issue.objects.filter(
            student=self.request.user,
            status=Status.objects.exclude(name="Closed")
            )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[""] = ""
    #     return context
    