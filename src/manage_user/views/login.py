
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.edit import UpdateView
from config.choice import RoleUser
from config.permission import LoginRequiredMixin
from manage_user.form.login import AdminPasswordChangeForm, LoginForm
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


class ChangePasswordAdminView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'component/form.html'
    form_class = AdminPasswordChangeForm

    def get_success_url(self):
        return '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_id = self.kwargs['user_id']
        user = AccountUser.objects.get(id=user_id)
        kwargs['user'] = user
        return kwargs

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user_id = self.kwargs['user_id']
        user = AccountUser.objects.get(id=user_id)
        context['header'] = f'Ganti Password {user}'
        context['header_title'] = f'Ganti Password {user}'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Sandi berhasil diubah.')
        return super().form_valid(form)
