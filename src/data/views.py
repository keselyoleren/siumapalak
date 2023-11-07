from pipes import Template
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from config.permission import LoginRequiredMixin


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    
class TrendingView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/trending.html"

class PerformenceView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/performence.html"

class HomeView(LoginRequiredMixin, TemplateView):
    
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return 'dashboard/index.html'
        return 'home.html'
    

class SchemaView(TemplateView):
    template_name = "schema.html"

class KeteranganView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/keterangan.html"