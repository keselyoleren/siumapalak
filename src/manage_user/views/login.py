
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.edit import UpdateView
from config.choice import RoleUser
from config.permission import IsLoginAuthenticated
from manage_user.form.login import LoginForm
from manage_user.models import AccountUser
from django.contrib.auth.views import PasswordChangeView

class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    def get_success_url(self) -> str:
        return "/dashboard"

