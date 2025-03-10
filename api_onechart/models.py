from django.db import models

class Clube(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    gols = models.IntegerField()

    def __str__(self):
        return self.nome

class Partida(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    adversario = models.CharField(max_length=255)
    resultado = models.CharField(max_length=50) 

    def __str__(self):
        return self.adversario

class Torcida(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    total = models.IntegerField()
    socios = models.IntegerField()
    seguidores = models.IntegerField()

    def __str__(self):
        return self.total

class Ranking(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Estatisticas(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    ranking = models.ForeignKey(Ranking, on_delete=models.CASCADE)
    titulos = models.IntegerField()

    def __str__(self):
        return self.titulos
