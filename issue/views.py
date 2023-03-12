from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import CreateIssueForm, UpdateIssueForm
from .models import Issue, MyGroup, Status

class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    paginate_by = 50

    def get_queryset(self):
        """ Return filtered list of issues for student or agent """
        #revert back to 3.9 compat, as django docker-compose is v3.9 LS
        view = self.request.user.active_view
        if view == 'Open': qs = Issue.openIssues.all()
        if view == 'New': qs = Issue.openIssues.filter(status__name='New')
        if view == 'Assigned': qs = Issue.objects.filter(status__name='Assigned')
        if view == 'In Progress': qs = Issue.objects.filter(status__name='In Progress')
        if view == 'Referred': qs = Issue.objects.filter(status__name='Referred')
        if view == 'Escalated': qs = Issue.objects.filter(escalation__name__in=['Level2','Level3'])
        if view == 'Resolved': qs = Issue.objects.filter(status__name='Resolved')
        if view == 'Closed': qs = Issue.closedIssues.all()
        if view == 'Deleted': qs = Issue.objects.filter(status__name='Deleted')
        if not self.request.user.is_support_agent():
            qs = qs.filter(student=self.request.user)
        return qs

    def get(self, request, *args, **kwargs):
        request.user.active_view = request.GET.get('filter','Open')
        request.user.save()
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['createIssueForm'] = CreateIssueForm
        context['updateIssueForm'] = UpdateIssueForm
        return context

class IssueCreateView(LoginRequiredMixin, CreateView):
    success_message = "Your issue was added, we'll be in touch soon."
    success_url = reverse_lazy('issue:home')
    form_class = CreateIssueForm
    template_name = 'issue/issue_list.html'
    model = Issue

    def form_valid(self, form, request):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.student = request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)
        
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    success_url = reverse_lazy('issue:home')
    form_class = UpdateIssueForm
    template_name = 'issue/issue_update.html'
    model = Issue

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        submitButtons = ['Update','Escalate','Resolve','Close']
        btn = [btn for btn in submitButtons if btn in request.POST][0]

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, btn)
        return self.form_invalid(form)

    def test_func(self):
        obj = self.get_object()
        staff = bool(self.request.user.is_support_agent())
        myself = bool(obj.student == self.request.user)
        safe = bool(self.request.method == 'GET' or 
                    'Escalate' not in self.request.POST)
        return staff or (myself and safe)
    
    def form_valid(self, form, btn):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        if btn == 'Escalate':
            if self.object.escalation_id == MyGroup.Level1Id():
                self.object.escalation_id = MyGroup.Level2Id()
            else:
                self.object.escalation_id = MyGroup.Level3Id()
        if btn == 'Resolve':
            self.object.status_id = Status.ResolvedId()
        if btn == 'Closed':
            self.object.status_id = Status.ClosedId()
        self.object.save()
        return super().form_valid(form)