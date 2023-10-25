from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class DashboardView(TemplateView):
    template_name = "dashboard/index.html"
    
class TrendingView(TemplateView):
    template_name = "dashboard/trending.html"

class PerformenceView(TemplateView):
    template_name = "dashboard/performence.html"


class HomeView(TemplateView):
    template_name = "home.html"


class SchemaView(TemplateView):
    template_name = "schema.html"

class KeteranganView(TemplateView):
    template_name = "dashboard/keterangan.html"