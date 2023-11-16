from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='Lista Produtos'),
    path('<slug>', views.DetalheProdutos.as_view(), name='Detalhe Produto'),
    path('addcar/', views.AddCar.as_view(), name='Adiciona Carrinho'),
    path('delcar/', views.DelCar.as_view(), name='Deleta Carrinho'),
    path('car/', views.Car.as_view(), name='Carrinho'),
    path('resumo/', views.Resumo.as_view(), name='Resumo da compra'),
]
