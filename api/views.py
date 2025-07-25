from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.request import Request
from data.models import MaioresDividendos, MaioresLucros, MaioresDividendosMedio
from .serializer import MaioresDividendosSerializer, MaioresLucrosSerializer, MaioresDividendosMedioSerializer
from datetime import date

class HomePageView(APIView):
    def get(self, request):
        return Response({
            "Endpoints": {
                "Maiores Dividendos": request.build_absolute_uri('/api/maiores-dividendos/'),
                "Top 10 Maiores Dividendos": request.build_absolute_uri('/api/top10-dividendos/'),
                
                "Maiores Dividendos Médio": request.build_absolute_uri('/api/maiores-dividendos-medio/'),
                
                "Maiores Lucros": request.build_absolute_uri('/api/maiores-lucros/'),
                "Top 10 Maiores Lucros": request.build_absolute_uri('/api/top10-maiores-lucros/')
            }
        })

class MaioresDividendosView(APIView):
    def get(self, request):
        maioresDividendos = MaioresDividendos.objects.order_by('-dividendo_atual')
        serializer = MaioresDividendosSerializer(maioresDividendos, many=True)
        return Response(serializer.data)

class MaioresDividendosMedioView(APIView):
    def get(self, request):
        maioresDividendosMedio = MaioresDividendosMedio.objects.order_by('-dividendo_medio')
        serializer = MaioresDividendosMedioSerializer(maioresDividendosMedio, many=True)
        return Response(serializer.data)

class Top10MaioresDividendosView(APIView):
    def get(self, request):
        hoje = date.today()
        top_dividendo = MaioresDividendos.objects.filter(data=hoje).order_by('-dividendo_atual')[:10]
        serializer = MaioresDividendosSerializer(top_dividendo, many=True)
        return Response(serializer.data)

class Top10MaioresDividendosMedioView(APIView):
    def get(self, request):
        top_dividendo = MaioresDividendos.objects.order_by('-dividendo_medio')[:10]
        serializer = MaioresDividendosSerializer(top_dividendo, many=True)
        return Response(serializer.data)

class MaioresLucrosView(APIView):
    def get(self, request):
        maioresLucros = MaioresLucros.objects.order_by('-lucro')
        serializer = MaioresLucrosSerializer(maioresLucros, many=True)
        return Response(serializer.data)

class Top10MaioresLucrosView(APIView):
    def get(self, request):
        hoje = date.today()  # Data de hoje
        # Filtra os registros com data igual a hoje e ordena decrescentemente por lucro
        top_maiores_lucros = MaioresLucros.objects.filter(data=hoje).order_by('-lucro')[:10]
        
        # Serializa os dados para resposta JSON
        serializer = MaioresLucrosSerializer(top_maiores_lucros, many=True)
        return Response(serializer.data)
    
    