from rest_framework import viewsets
from api_onechart import models
from api_onechart.api import serializers

class ClubeViewSet(viewsets.ModelViewSet):
    queryset = models.Clube.objects.all()
    serializer_class = serializers.ClubeSerializer

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = models.Jogador.objects.all()
    serializer_class = serializers.JogadorSerializer

class PartidaViewSet(viewsets.ModelViewSet):
    queryset = models.Partida.objects.all()
    serializer_class = serializers.PartidaSerializer

class TorcidaViewSet(viewsets.ModelViewSet):
    queryset = models.Torcida.objects.all()
    serializer_class = serializers.TorcidaSerializer

class RankingViewSet(viewsets.ModelViewSet):
    queryset = models.Ranking.objects.all()
    serializer_class = serializers.RankingSerializer

class EstatisticasViewSet(viewsets.ModelViewSet):
    queryset = models.Estatisticas.objects.all()
    serializer_class = serializers.EstatisticasSerializer