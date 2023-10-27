
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.edit import UpdateView
from config.choice import RoleUser
from config.permission import LoginRequiredMixin
from manage_user.form.login import LoginForm
from manage_user.models import AccountUser
from django.contrib.auth.views import PasswordChangeView

class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    # redirect_field_name = '/dashboard'

    def get_success_url(self) -> str:
        return "/dashboard"

class UserLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)
