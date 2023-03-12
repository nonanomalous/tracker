from django import forms

from .models import Issue

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['brief','description','subcategory','escalation']
        widgets = {
            'brief': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'escalation': forms.HiddenInput(attrs={'readonly': 'readonly'}),
        }

class UpdateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['brief','description','subcategory']
        widgets = {
            'brief': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
        }
