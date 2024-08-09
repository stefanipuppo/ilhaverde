from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.pedido_novo, name='pedido_novo'),
    path('lista/', views.pedido_lista, name='pedido_lista'),
]
