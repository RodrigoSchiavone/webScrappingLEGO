from mercado_livre import mercado_livre

lista = [['10981','Cenoura-Crescendo'],['31138','Trailer-de-Praia']]

i = 0
product = []
while i < len(lista):
    url = "https://lista.mercadolivre.com.br/lego-"+lista[i][0]+"-"+lista[i][1]
    product.append(mercado_livre(url))
    i += 1

i = 0
j = 0

while i<len(product):
    while j<len(product[i][0]):
        print(product[i][0][j]+' '+product[i][1][j]+' '+product[i][2][j])
        print("_____________________________________________________________________")
        j += 1
    
    i += 1
    j = 0