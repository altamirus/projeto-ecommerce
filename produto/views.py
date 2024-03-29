from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 6


class DetalheProdutos(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AddCar(View):
    def get(self, *args, **kwargs):
        # Usado para limpar a sessao do carrinho de compra
        # if self.request.session.get('car'):
        #     del self.request.session['car']
        #     self.request.session.save()

        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:Lista Produtos')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto nao existe'
            )
            return redirect(http_referer)
        variacao = get_object_or_404(models.Variacao, id=variacao_id)
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)

        if not self.request.session.get('car'):
            self.request.session['car'] = {}
            self.request.session.save()
        car = self.request.session['car']

        if variacao_id in car:
            quantidade_atual = car[variacao_id]['quantidade']
            quantidade_atual += 1

            if variacao_estoque < quantidade_atual:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {quantidade_atual}x no '
                    f'produto "{produto_nome}". Adicionamos {variacao_estoque}x'
                    f'no seu carrinho.'
                )
                quantidade_atual = variacao_estoque

            car[variacao_id]['quantidade'] = quantidade_atual
            car[variacao_id]['preco_quantitativo'] = preco_unitario * \
                quantidade_atual

            car[variacao_id]['preco_unitario_promocional'] = preco_unitario_promocional * quantidade_atual

        else:
            car[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional,
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocional': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
            }
        self.request.session.save()

        messages.success(
            self.request,
            f'Produto {produto_nome}{variacao_nome} adicionado ao seu '
            f'carrinho {car[variacao_id]["quantidade"]}x.'
        )
        return redirect(http_referer)


class DelCar(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:Lista Produtos')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            return redirect(http_referer)

        if not self.request.session.get('car'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['car']:
            return redirect(http_referer)

        car = self.request.session['car'][variacao_id]

        messages.success(
            self.request,
            f' Produto {car["produto_nome"]}{car["variacao_nome"]}'
            f' removido do seu carrinho.'
        )

        del self.request.session['car'][variacao_id]
        self.request.session.save()
        return redirect(http_referer)


class Car(View):
    def get(self, *args, **kwargs):
        contexto = {
            'car': self.request.session.get('car', {})
        }
        return render(self.request, 'produto/carrinho.html', contexto)


class Resumo(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
