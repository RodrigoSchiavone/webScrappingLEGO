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
    j = 1
    while i < len(cards):

        div = cards[i].contents[0]
        a = div.find('a')
        if a != None:
            name = a.find('h2').string
            url = a['href']
        else:
            name = 'invalid'
            url = 'invalid'
            print('"a" NoneType')



        divPrice = cards[i].contents[1]
        
        divPrice2 = divPrice.find('span', class_="price-tag ui-search-price__part shops__price-part")
        if divPrice2 != None:
            #print(len(divPrice.find_all('div', class_="ui-search-price ui-search-price--size-medium shops__price")))
            priceAmount = divPrice2.find('span', class_="price-tag-amount")
        

            price_fraction = priceAmount.find('span', class_="price-tag-fraction")
            price_cents = priceAmount.find('span', class_="price-tag-cents")

            if price_cents != None:
                price = price_fraction.string+','+price_cents.string
            else:
                price = price_fraction.string+',00'
        else:
            price = '0,00'
            print('price NoneType')
    

        lenPesquisa = len(pesquisa)
        pesquisaStr =  pesquisa.replace('-', ' ')
        regex1 = '.*'+str(codLEGO)+'.*'
        regex2 = '.*Manual*.'
        #regex2 = '.*'+pesquisaStr[int(lenPesquisa / 2):]+'.*Lego*.'
        #regex3 = '.*Lego*.'+pesquisaStr[int(lenPesquisa / 2):]+'.*'
        #
       
        testRegex1 = re.match(regex1, name)
        testRegex2 = re.match(regex2, name)
        #testRegex3 = re.match(regex3, name)
        #testRegex4 = re.match(regex4, name)


        if testRegex1 != None and testRegex2 == None: #or testRegex2 != None or testRegex3 != None) and testRegex4 == None:
            #print(str(codLEGO) + ' >> '+nome)
            itens.append({'codLEGO':codLEGO,'pesquisa':pesquisa,'nome': name, 'preco': price,'data': data, 'url': url})
            #print('')

        i += 1
   
    
    dataframe = pd.DataFrame(itens)
    #print(dataframe)
    print(str(codLEGO) + ' ' + pesquisa)
    print('____________________________________________________________________________')
    return dataframe