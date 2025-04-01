from rest_framework import viewsets
from api_onechart import models
from api_onechart.api import serializers
from drf_yasg.utils import swagger_auto_schema

class ClubeViewSet(viewsets.ModelViewSet):
    queryset = models.Clube.objects.all()
    serializer_class = serializers.ClubeSerializer
    @swagger_auto_schema(
        operation_description="Listar todas os Clubes",
        responses={200: serializers.ClubeSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cria um nova Clube",
        responses={201:"Clube criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="retorna o clube conforme ID e dados informados",
        responses={200: "Clube alterado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Altera o Clube conforme ID e dados informados",
        responses={200: "Clube alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Deleta o Clube conforme ID informado",
        responses={204: "Clube deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = models.Jogador.objects.all()
    serializer_class = serializers.JogadorSerializer
    @swagger_auto_schema(
        operation_description="Listar todas os Jogadores",
        responses={200: serializers.JogadorSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="adiciona um jogador",
        responses={201:"Jogador criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="retorna o Jogador conforme ID e dados informados",
        responses={200: "Jogador alterado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Altera o Jogador conforme ID e dados informados",
        responses={200: "Jogador alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Deleta o Jogador conforme ID informado",
        responses={204: "Jogador deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class PartidaViewSet(viewsets.ModelViewSet):
    queryset = models.Partida.objects.all()
    serializer_class = serializers.PartidaSerializer
    @swagger_auto_schema(
        operation_description="Listar todas as partidas",
        responses={200: serializers.PartidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cria uma nova partida",
        responses={201:"Partida criada com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="retorna a partida conforme ID e dados informados",
        responses={200: "Partida alterada com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Altera a partida conforme ID e dados informados",
        responses={200: "Partida alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Deleta a parrtida conforme ID informado",
        responses={204: "Partida deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class TorcidaViewSet(viewsets.ModelViewSet):
    queryset = models.Torcida.objects.all()
    serializer_class = serializers.TorcidaSerializer
    @swagger_auto_schema(
        operation_description="Listar todas as Torcidas",
        responses={200: serializers.TorcidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cria uma nova torcida",
        responses={201:"Torcida criada com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="retorna a tprcida conforme ID e dados informados",
        responses={200: "Torcida alterado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Altera a torcida conforme ID e dados informados",
        responses={200: "Torcida alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Deleta a torcida conforme ID informado",
        responses={204: "Torcida deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class RankingViewSet(viewsets.ModelViewSet):
    queryset = models.Ranking.objects.all()
    serializer_class = serializers.RankingSerializer
    @swagger_auto_schema(
        operation_description="Listar todos os rankings",
        responses={200: serializers.RankingSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cria um novo ranking",
        responses={201:"Ranking criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="retorna o ranking conforme ID e dados informados",
        responses={200: "Ranking alterado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Altera o Ranking conforme ID e dados informados",
        responses={200: "Ranking alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Deleta o Ranking conforme ID informado",
        responses={204: "Ranking deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class EstatisticasViewSet(viewsets.ModelViewSet):
    queryset = models.Estatisticas.objects.all()
    serializer_class = serializers.EstatisticasSerializer
    @swagger_auto_schema(
        operation_description="Listar todas os Clubes",
        responses={200: serializers.EstatisticasSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Cria uma nova estatistica",
        responses={201:"Estatistica criado com sucesso"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="retorna a estatistica conforme ID e dados informados",
        responses={200: "Estatistica alterado com sucesso"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Altera a estatistica conforme ID e dados informados",
        responses={200: "Estatisticas alterado com sucesso"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Deleta a estatistica conforme ID informado",
        responses={204: "Estatica deletada com sucesso"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)