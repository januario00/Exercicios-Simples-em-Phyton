#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

import requests

def pegar_valor_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    valor_dolar = float(dados["USDBRL"]["bid"])
    return valor_dolar


# Teste simples : passo a passo para a pesca de dados em banco

#def pegar_carta(): (importa o módulo)
#caixa_postal = "URL" (url do banco)
#envelope = requests.get(caixa_postal)  (capta os dados usando request)
#conteudo = envelope.json()        (converte em.json)
#return conteudo                   (usa os dados)



real = (float(input('Digite o valor R$')))
total = real / pegar_valor_dolar()
print(f"Você consegue comprar ${total:.2f}")
