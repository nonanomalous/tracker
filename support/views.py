from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from issue.models import Document

# citation https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
class DocumentCreateView(CreateView):
    model = Document
    fields = ['file', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context