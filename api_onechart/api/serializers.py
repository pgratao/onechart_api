from rest_framework import serializers
from api_onechart import models

class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clube
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do clube'},
            'nome': {'help_text': 'Nome do clube'},
        }

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jogador
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do jogador'},
            'nome': {'help_text': 'Nome do jogador'},
            'clube': {'help_text': 'Informar o ID do clube ao qual o jogador pertence'},
            'posicao': {'help_text': 'Posição em que o jogador atua'},
        }

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da partida'},
            'data': {'help_text': 'Data da partida'},
            'local': {'help_text': 'Local onde a partida foi realizada'},
            'clube_mandante': {'help_text': 'ID do clube mandante'},
            'clube_visitante': {'help_text': 'ID do clube visitante'},
            'placar': {'help_text': 'Placar final da partida'},
        }

class TorcidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Torcida
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da torcida'},
            'clube': {'help_text': 'ID do clube ao qual a torcida pertence'},
            'quantidade_membros': {'help_text': 'Número de membros da torcida'},
        }

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ranking
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador do ranking'},
            'clube': {'help_text': 'ID do clube no ranking'},
            'posicao': {'help_text': 'Posição do clube no ranking'},
            'pontos': {'help_text': 'Pontuação do clube'},
        }

class EstatisticasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estatisticas
        fields = '__all__'
        extra_kwargs = {
            'id': {'help_text': 'Identificador da estatística'},
            'jogador': {'help_text': 'ID do jogador ao qual as estatísticas pertencem'},
            'gols': {'help_text': 'Número de gols marcados pelo jogador'},
            'assistencias': {'help_text': 'Número de assistências feitas pelo jogador'},
            'partidas_jogadas': {'help_text': 'Número de partidas jogadas pelo jogador'},
        }
