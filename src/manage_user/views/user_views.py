# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from config.choice import RoleUser

from config.permission import LoginRequiredMixin
from manage_user.form.user_form import AccountUserForm, UserForm
from manage_user.models import AccountUser


class AccountUserListView(LoginRequiredMixin, ListView):
    model = AccountUser
    template_name = 'users/list.html'
    context_object_name = 'list_users'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'List User'
        context['btn_add'] = True
        context['create_url'] = reverse_lazy('user-create')
        return context

class AccountUserCreateView(LoginRequiredMixin, CreateView):
    model = AccountUser
    template_name = 'component/form.html'
    form_class = AccountUserForm
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'Tambah User'
        return context

    def form_valid(self, form):
        if form.cleaned_data.get('role_user') == RoleUser.OPERATOR:
            form.instance.is_superuser = True
        return super().form_valid(form)

class AccountUserUpdateView(LoginRequiredMixin, UpdateView):
    model = AccountUser
    template_name = 'component/form.html'
    form_class = UserForm
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'Edit User'
        return context

    def form_valid(self, form):
        if form.cleaned_data.get('role_user') == RoleUser.OPERATOR:
            form.instance.is_superuser = True
        else:
            form.instance.is_superuser = False
        return super().form_valid(form)

class AccountUserDeleteView(LoginRequiredMixin, DeleteView):
    model = AccountUser
    template_name = 'component/delete.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'Delete User'
        return context
