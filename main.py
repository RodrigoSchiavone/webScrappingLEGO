from mercado_livre import mercado_livre

url = "https://lista.mercadolivre.com.br/lego-10696"

product = mercado_livre(url)

i = 0
while i<len(product[0]):
    print(product[0][i]+" >> "+product[1][i]+" >> "+product[2][i])
    print("_____________________________________________________________________")
    i += 1