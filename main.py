from mercado_livre import mercado_livre
from amazon import amzon
import pandas as pd
from unidecode import unidecode

product = []
#lista = [['10981','Cenoura-Crescendo'],['31138','Trailer-de-Praia']]
#pip install requests_html pandas unidecode openpyxl

i = 0

dataframe = pd.read_excel('test.xlsx')
dictionary = dataframe.to_dict()
print(dictionary['codLEGO'][0])

codLEGO = []
for item in dictionary['nome']:
    
    dictionary['nome'][item] = dictionary['nome'][item].replace('-',' ')
    dictionary['nome'][item] = dictionary['nome'][item].replace(' ','-')
    dictionary['nome'][item] = dictionary['nome'][item].replace('™','')
    dictionary['nome'][item] = dictionary['nome'][item].replace('®','')
    dictionary['nome'][item] = dictionary['nome'][item].replace('(','')
    dictionary['nome'][item] = dictionary['nome'][item].replace(')','')
    dictionary['nome'][item] = unidecode(dictionary['nome'][item])

    dictionary['codLEGO'][item] = str(dictionary['codLEGO'][item])
   
    i += 1
#print(dictionary)
#™ ®
itens = []
i = 0
while i < len(dictionary['codLEGO']):
    
    url = "https://lista.mercadolivre.com.br/lego-"+dictionary['codLEGO'][i]+"-"+dictionary['nome'][i]
    product = mercado_livre(url, itens, dictionary['codLEGO'][i],dictionary['nome'][i])
    i += 1

print(product)
product.to_excel('./precos_mercado_livre.xlsx', index=False)

i = 0

while i < len(dictionary['codLEGO']):
    
    url = "https://www.amazon.com.br/s?k=lego-"+dictionary['codLEGO'][i]+"-"+dictionary['nome'][i]
    product = amzon(url, itens, dictionary['codLEGO'][i],dictionary['nome'][i])
    i += 1

#print(product)
product.to_excel('./precos_amazon.xlsx', index=False)

