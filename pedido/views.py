from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pedido
from .forms import PedidoForm

def pedido_novo(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido realizado com sucesso!')
            return redirect('pedido_novo') 
    else:
        form = PedidoForm()
    return render(request, 'pedido/pedido_form.html', {'form': form})



def pedido_lista(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/pedido_lista.html', {'pedidos': pedidos})