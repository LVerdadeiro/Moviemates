from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, Sessao, Assento, Reserva, Produto

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'lista_filmes.html', {'filmes': filmes})

def detalhe_sessao(request, sessao_id):
    sessao = get_object_or_404(Sessao, id=sessao_id)
    assentos = Assento.objects.filter(sessao=sessao)
    return render(request, 'detalhe_sessao.html', {'sessao': sessao, 'assentos': assentos})

def reservar_assento(request, assento_id):
    assento = get_object_or_404(Assento, id=assento_id)
    if assento.disponivel:
        assento.disponivel = False
        assento.save()
        Reserva.objects.create(usuario=request.user, assento=assento)
    return redirect('detalhe_sessao', sessao_id=assento.sessao.id)

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})
