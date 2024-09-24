from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField()
    duracao = models.DurationField()

class Sessao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    horario = models.DateTimeField()

class Assento(models.Model):
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    disponivel = models.BooleanField(default=True)

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    assento = models.ForeignKey(Assento, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    loja = models.CharField(max_length=100)  # Exemplo de vinculação com outras lojas
