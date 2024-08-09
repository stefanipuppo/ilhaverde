from django.db import models
from core.models import Planta

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_entrega = models.DateField()
    planta = models.ManyToManyField(Planta, through='PedidoPlanta', related_name='pedidos')

    def __str__(self):
        return f'Pedido {self.id} para {self.cliente}'

class PedidoPlanta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} de {self.planta} no Pedido {self.pedido}'