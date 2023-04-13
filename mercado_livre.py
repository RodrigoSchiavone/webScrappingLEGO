from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pprint
import re
import pandas as pd
from datetime import date

def mercado_livre(text,itens,codLEGO,pesquisa):
    s = HTMLSession()
    url = text
    
    codLEGO = int(codLEGO)
    pesqiusa = pesquisa
    data = date.today()

    def getdata(url):
        r = s.get(url)
        print(r)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
        

    html = getdata(url)
    

    h2 = html.find_all('h2', class_="ui-search-item__title shops__item-title")

    price = []

    span = html.find_all('span', class_="price-tag ui-search-price__part shops__price-part")

    
    i = 0
    while i<len(span):
        span2 = span[i].find('span',class_="price-tag-amount")
        price_fraction = span2.find('span', class_="price-tag-fraction")
        price_cents = span2.find('span', class_="price-tag-cents")

        if(price_cents != None):
            price.append(price_fraction.string+","+price_cents.string)
        else:
            price.append(price_fraction.string+","+"00")
        i += 2
    card = html.find_all('div', {'class':re.compile('andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core.*')})
                                                     
   
    i = 0 
    while i < len(h2):

        nome = h2[i].string

        preco = float(price[i].replace(',','.'))

        div = card[i].contents[0]
        a = div.contents[0]
        url = a['href']
        i += 1
        itens.append({'codLEGO':codLEGO,'pesquisa':pesquisa,'nome': nome, 'preco': preco,'data': data, 'url': url})

 
    dataframe = pd.DataFrame(itens)
    #print(dataframe)
    return dataframe