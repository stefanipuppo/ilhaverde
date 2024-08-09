from django.contrib import admin
from pedido.models import Pedido  
from .models import Planta, Venda, Cliente

admin.site.register(Planta)
admin.site.register(Venda)
admin.site.register(Cliente)
admin.site.register(Pedido)