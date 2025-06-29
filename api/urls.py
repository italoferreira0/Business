from django.urls import path
from .views import  HomePageView, MaioresDividendosView, Top10MaioresDividendosView, MaioresDividendosMedioView , MaioresLucrosView,Top10MaioresLucrosView

urlpatterns = [
    path('maiores-dividendos/', MaioresDividendosView.as_view(), name='maiores-dividendos'),
    path('top10-dividendos/', Top10MaioresDividendosView.as_view(), name='top10-dividendos'),
    path('maiores-dividendos-medio/', MaioresDividendosMedioView.as_view(), name='maiores-dividendos-medio'),

    path('maiores-lucros/', MaioresLucrosView.as_view(), name='maiores-lucros'),
    path('top10-maiores-lucros/', Top10MaioresLucrosView.as_view(), name='top10-maiores-lucros'),
    path('', HomePageView.as_view(), name='api'),
]