from django.db import models

class Planta(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_entrega = models.DateField()
    planta = models.ManyToManyField(Planta, through='PedidoPlanta')

    def __str__(self):
        return f'Pedido {self.id} para {self.cliente}'


class PedidoPlanta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

class Venda(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Venda de {self.quantidade} {self.planta.nome} (s)'