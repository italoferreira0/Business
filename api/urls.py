from django.urls import path
from .views import MaioresDividendosView, MaioresLucrosView

urlpatterns = [
    path('maiores-dividendos/', MaioresDividendosView.as_view(), name='maiores-dividendos'),
    path('maiores-lucros/', MaioresLucrosView.as_view(), name='maiores-lucros'),
]