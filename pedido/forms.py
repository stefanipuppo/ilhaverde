from django import forms
from .models import Pedido, PedidoPlanta

class PedidoPlantaForm(forms.ModelForm):
    class Meta:
        model = PedidoPlanta
        fields = ['planta', 'quantidade']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'email', 'data_entrega', 'planta']
        widgets = {
            'data_entrega': forms.DateInput(attrs={'type': 'date'}),
        }