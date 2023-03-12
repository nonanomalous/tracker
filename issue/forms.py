from django import forms

from .models import Issue

class CreateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['brief','description','subcategory','student','escalation']
        widgets = {
            'brief': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'student': forms.HiddenInput(),
            'escalation': forms.TextInput(),
        }

class UpdateIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['brief','description','subcategory','student']
        widgets = {
            'brief': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'student': forms.HiddenInput(attrs={'readonly': 'readonly'}),
        }
