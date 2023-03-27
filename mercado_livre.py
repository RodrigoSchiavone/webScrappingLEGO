from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pprint

def mercado_livre(text):
    s = HTMLSession()
    url = text



    def getdata(url):
        r = s.get(url)
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

    link = html.find_all('a', class_="ui-search-link")

    i = 0 
    product = [[],[],[]]
    while i < len(h2):
        product[0].append(h2[i].string)
        product[1].append(price[i])
        product[2].append(link[i].get('href'))
        i += 1
    
        
    return product
   
    
     
mercado_livre("https://lista.mercadolivre.com.br/lego-10696")