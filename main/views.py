from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class AnaliseView(TemplateView):
    template_name = 'analise.html'

class CarteiraView(TemplateView):
    template_name = 'carteira.html'