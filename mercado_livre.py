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
     
    cards = html.find_all('div',class_="ui-search-result__content-wrapper shops__result-content-wrapper")


    i = 0
    while i < len(cards):

        div = cards[i].contents[0]
        a = div.find('a')

        name = a.find('h2').string
        url = a['href']



        divPrice = cards[i].contents[1]

        divPrice2 = divPrice.find('span', class_="price-tag ui-search-price__part shops__price-part")

        #print(len(divPrice.find_all('div', class_="ui-search-price ui-search-price--size-medium shops__price")))
        priceAmount = divPrice2.find('span', class_="price-tag-amount")
        

        price_fraction = priceAmount.find('span', class_="price-tag-fraction")
        price_cents = priceAmount.find('span', class_="price-tag-cents")

        if price_cents != None:
            price = price_fraction.string+','+price_cents.string
        else:
            price = price_fraction.string+',00'
        
    
        lenPesquisa = len(pesquisa)
        pesquisaStr =  pesquisa.replace('-', ' ')
        regex1 = '.*'+str(codLEGO)+'.*'
        regex2 = '.*'+pesquisaStr[int(lenPesquisa / 2):]+'.*'
       


        if re.match(regex1, name) or re.match(regex2, name):
            #print(str(codLEGO) + ' >> '+nome)
            itens.append({'codLEGO':codLEGO,'pesquisa':pesquisa,'nome': name, 'preco': price,'data': data, 'url': url})
            print('')

        i += 1
   
    
    dataframe = pd.DataFrame(itens)
    #print(dataframe)
    print(str(codLEGO) + ' ' + pesquisa)
    print('____________________________________________________________________________')
    return dataframe