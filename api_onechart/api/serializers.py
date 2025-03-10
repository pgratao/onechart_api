from rest_framework import serializers
from api_onechart import models

class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clube
        fields = '__all__'

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jogador
        fields = '__all__'

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partida
        fields = '__all__'

class TorcidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Torcida
        fields = '__all__'

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ranking
        fields = '__all__'

class EstatisticasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estatisticas
        fields = '__all__'
