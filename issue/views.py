from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView

from issue.models import Issue, Status

class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    paginate_by = 50

    def filter_by_active_view():
        pass

    def get_queryset(self):
        
        match self.request.user.active_view:
            case 'Closed': qs = Issue.closedIssues.all()
            case 'Open': qs = Issue.openIssues.all()
            case 'Solved': qs = Issue.openIssues.filter()
        if not self.request.user.is_support_agent():
            qs = qs.filter(student=self.request.user)
        return qs


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[""] = ""
    #     return context
    