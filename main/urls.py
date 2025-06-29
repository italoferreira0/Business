from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('analise/', AnaliseView.as_view(), name='analise'),
    path('carteira/', CarteiraView.as_view(), name='carteira'),
]