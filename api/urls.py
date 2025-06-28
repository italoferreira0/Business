from django.urls import path
from .views import MaioresDividendosView, MaioresLucrosView, HomePageView

urlpatterns = [
    path('maiores-dividendos/', MaioresDividendosView.as_view(), name='maiores-dividendos'),
    path('maiores-lucros/', MaioresLucrosView.as_view(), name='maiores-lucros'),
    path('', HomePageView.as_view(), name='api'),
]