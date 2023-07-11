from requests_html import HTMLSession
from bs4 import BeautifulSoup
from prettyprinter import pprint
import re
import pandas as pd
from datetime import date

def amzon(text,itens,codLEGO,pesquisa):

    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    s = HTMLSession()
    url = text

    codLEGO = int(codLEGO)
    pesqiusa = pesquisa
    data = date.today()

    def getdata(url):
        r = s.get(url,headers = HEADERS)
        print(r)
        if not r:
            getdata(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
        

    html = getdata(url)

    cards = html.find_all('div', class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

    #print(cards[0])
    i = 0
    while i < len(cards):
        div = cards[i]
        h2 = div.find('h2')
        a = h2.find('a')

        if a['href'] != None: 
            name = a.contents[0].string
            link = "https://www.amazon.com.br"+a['href']
            #print(name)
            #print(link)
            
        else:
            nome = 'invalid'
            print('invalid name')

        spanPrice = div.find('span',class_='a-price')

        if spanPrice != None:
            price = spanPrice.contents[0].text
            price = price.replace('R$', '')
            price = price.replace(' ','')
            #print(price)
        else:
            price = '0,00'
            print('invalid price')

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
            itens.append({'codLEGO':codLEGO,'pesquisa':pesquisa,'nome': name, 'preco': price,'data': data, 'url': link,'marketplace':'amazon'})
            #print('')
        
        i += 1
    
    dataframe = pd.DataFrame(itens)
    #print(dataframe)
    print(str(codLEGO) + ' ' + pesquisa)
    print('Amazon')
    print('____________________________________________________________________________')
    return dataframe