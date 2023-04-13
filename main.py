from mercado_livre import mercado_livre
import pandas as pd


lista = [['10981','Cenoura-Crescendo'],['31138','Trailer-de-Praia']]

i = 0
product = []


itens = []
while i < len(lista):
    
    url = "https://lista.mercadolivre.com.br/lego-"+lista[i][0]+"-"+lista[i][1]
    product = mercado_livre(url, itens, lista[i][0],lista[i][1])
    i += 1

product.to_excel('./precos_mercado_livre.xlsx')

