from rest_framework import serializers
from data.models import MaioresDividendos, MaioresLucros, MaioresDividendosMedio

class MaioresDividendosSerializer(serializers.ModelSerializer):
    dividendo_atual = serializers.FloatField()
    dividendo_medio = serializers.FloatField()
    p_l = serializers.FloatField()
    p_vp = serializers.FloatField()
    margem_liquida = serializers.FloatField()
    valor_mercado = serializers.CharField()
    class Meta:
        model = MaioresDividendos
        fields = '__all__'

class MaioresDividendosMedioSerializer(serializers.ModelSerializer):
    dividendo_atual = serializers.FloatField()
    dividendo_medio = serializers.FloatField()
    p_l = serializers.FloatField()
    p_vp = serializers.FloatField()
    margem_liquida = serializers.FloatField()

    class Meta:
        model = MaioresDividendosMedio
        fields = ('__all__')

class MaioresLucrosSerializer(serializers.ModelSerializer):
    dividendo_medio = serializers.FloatField()
    p_l = serializers.FloatField()
    p_vp = serializers.FloatField()
    margem_liquida = serializers.FloatField()
    lucro = serializers.FloatField()
    class Meta:
        model = MaioresLucros
        fields = '__all__'
