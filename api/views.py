from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.request import Request
from data.models import MaioresDividendos, MaioresLucros
from .serializer import MaioresDividendosSerializer, MaioresLucrosSerializer

class HomePageView(APIView):
    def get(self, request):
        return Response({
            "Endpoints": {
                "Maiores Dividendos": request.build_absolute_uri('/api/maiores-dividendos/'),
                "Maiores Lucros": request.build_absolute_uri('/api/maiores-lucros/')
            }
        })

class MaioresDividendosView(APIView):
    def get(self, request):
        maioresDividendos = MaioresDividendos.objects.order_by('-setor')
        serializer = MaioresDividendosSerializer(maioresDividendos, many=True)
        return Response(serializer.data)
    
class MaioresLucrosView(APIView):
    def get(self, request):
        maioresLucros = MaioresLucros.objects.order_by('-setor')
        serializer = MaioresLucrosSerializer(maioresLucros, many=True)
        return Response(serializer.data)