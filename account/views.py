from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import AuthForm

class login_view(LoginView):
    form_class = AuthForm

def logout_view(request):
    logout(request)
    return redirect('login')