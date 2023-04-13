from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pprint
import re

def mercado_livre(text):
    s = HTMLSession()
    url = text



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
                                                     
    link = []
  
    i = 0 
    product = [[],[],[]]
    
    while i < len(h2):
        product[0].append(h2[i].string)
        product[1].append(price[i])
        div = card[i].contents[0]
        a = div.contents[0]
        product[2].append(a['href'])
        #print(product[0][i]+" >> "+product[1][i]+" >> "+product[2][i])
        #print("_____________________________________________________________________")
        i += 1

    return product