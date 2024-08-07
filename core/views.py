from django.shortcuts import render, get_object_or_404, redirect
from .models import Planta
from .forms import PlantaForm

def lista(request):
    plantas = Planta.objects.all()
    return render(request, 'core/lista.html', {'plantas': plantas})

def detalhes(request, pk):
    planta = get_object_or_404(Planta, pk=pk)
    return render(request, 'core/detalhes.html', {'planta': planta})

def planta_nova(request):
    if request.method == 'POST':
        form = PlantaForm(request.POST)
        if form.is_valid():
            planta = form.save()
            return redirect('detalhes', pk=planta.pk)
    else:
        form = PlantaForm()
    return render(request, 'core/editar.html', {'form': form})

def editar(request, pk):
    planta = get_object_or_404(Planta, pk=pk)
    if request.method == 'POST':
        form = PlantaForm(request.POST, instance=planta)
        if form.is_valid():
            planta = form.save()
            return redirect('detalhes', pk=planta.pk)
    else:
        form = PlantaForm(instance=planta)
    return render(request, 'core/editar.html', {'form': form})

def deletar(request, pk):
    planta = get_object_or_404(Planta, pk=pk)
    planta.delete()
    return redirect('lista')
