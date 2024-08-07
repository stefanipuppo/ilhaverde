from django.contrib import admin
from .models import Planta, Pedido, PedidoPlanta, Venda

admin.site.register(Planta)
admin.site.register(Pedido)
admin.site.register(PedidoPlanta)
admin.site.register(Venda)
