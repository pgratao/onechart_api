from django.db import models
import os
import uuid
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class RenameImage(object):
    def __init__(self, subdir='imagens'):
        self.subdir = subdir

    def __call__(self, insrance, filename):
        extension = filename.split('.')[-1]
        new_name = f"{uuid.uuid4()}.{extension}"
        return os.path.join(self.subdir,new_name)

class Clube(models.Model):
    nome = models.CharField(max_length=255)
    logotime = models.ImageField(upload_to=RenameImage('imagens/'))

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
