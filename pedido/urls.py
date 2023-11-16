from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name='Pagar'),
    path('salvarpedido/', views.SalvarPedido.as_view(), name='Salvar Pedido'),
    path('detalhe/', views.Detalhe.as_view(), name='Detalhes'),



]
