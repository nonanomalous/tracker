from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


class AuthForm(AuthenticationForm):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update({'class': 'form-control'})
      self.fields['password'].widget.attrs.update({'class': 'form-control'})

