from rest_framework import serializers
from data.models import MaioresDividendos, MaioresLucros

class MaioresDividendosSerializer(serializers.ModelSerializer):
    dividendo_atual = serializers.FloatField()
    dividendo_medio = serializers.FloatField()
    p_l = serializers.FloatField()
    p_vp = serializers.FloatField()
    margem_liquida = serializers.FloatField()

    class Meta:
        model = MaioresDividendos
        fields = ('__all__')

class MaioresLucrosSerializer(serializers.ModelSerializer):
    dividendo_medio = serializers.FloatField()
    p_l = serializers.FloatField()
    p_vp = serializers.FloatField()
    margem_liquida = serializers.FloatField()
    
    class Meta:
        model = MaioresLucros
        fields = '__all__'