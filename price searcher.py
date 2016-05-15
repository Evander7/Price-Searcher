import requests
from bs4 import BeautifulSoup
    
def glengarry_lookup(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    price_data = soup.find_all('span', {'class' : 'bold twentyfour'})
    if price_data == []:
        price_data = soup.find_all('span', {'class' : 'twentyfour'})
        if price_data == []:
            return 'Glengarrys', False
    price = float(price_data[0].text[1:])
    return 'Glengarrys', price

def liquormart_lookup(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    price_data = soup.find_all('span', {'class' : 'h1'})    
    price = float(price_data[0].text.strip()[3:])
    return 'Liquormart', price

def boozee_lookup(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    price_data = soup.find_all('span', {'class' : 'price'})
    if len(price_data) >= 2:
        price = price_data[1].text.strip()[1:]
    else:
        price = price_data[0].text.strip()[1:]
    price = float(price.strip())
    return 'Boozee.co.nz', price
    



#
el_jimador = {'name':'el jimador',
              'p_price': 40,
              'stores':
              [glengarry_lookup('http://www.glengarrywines.co.nz/items/92866/el+jimador+anejo+%28700ml%29'),
               liquormart_lookup('https://liquormart.co.nz/collections/tequila/products/el-jimador-anejo-700ml?variant=1077778933')]
              }
#
patron_chocolate = {'name':'Patron XO Dark Cocoa',
                    'p_price':75,
                    'stores':
                    [glengarry_lookup('http://www.glengarrywines.co.nz/items/92143/patron+xo+cafe+dark+cocoa'),
                     liquormart_lookup('https://liquormart.co.nz/collections/tequila/products/patron-xo-cafe-dark-cocoa-30-750ml?variant=1104333421')]

    }
#
casa_noble_rep = {'name':'Casa Noble Reposado',
                  'p_price': 115,
                  'stores':
                  [glengarry_lookup('http://www.glengarrywines.co.nz/items/93178/casa+noble+tequila+reposado+%28750ml%29'),
                   boozee_lookup('http://boozee.co.nz/casa-noble-anejo-tequila.html')]
    }

#
agavero = {'name':'Agavero',
           'p_price': 80,
              'stores':
              [boozee_lookup('http://boozee.co.nz/jose-cuervo-agavero.html'),
               liquormart_lookup('https://liquormart.co.nz/collections/tequila/products/jose-cuervo-agavero-tequila-750ml?variant=851377665')]
              }
#
_1800_coconut = {'name':'1800 Coconut',
           'p_price': 65,
              'stores':
              [liquormart_lookup('https://liquormart.co.nz/collections/tequila/products/jose-cuervo-1800-coco-35-750ml?variant=6531884289')]
              }
#
corralejo_rep ={'name':'Corralejo Reposado',
           'p_price': 70,
              'stores':
              [liquormart_lookup('https://liquormart.co.nz/collections/tequila/products/corralejo-reposado-tequila-750ml?variant=16366084865')]
              }
#
arette ={'name':'Arette Anejo',
           'p_price': 70,
              'stores':
              [liquormart_lookup('https://liquormart.co.nz/collections/tequila/products/arette-tequila-anejo?variant=12171017537')]
              }
#

products = [el_jimador, patron_chocolate, casa_noble_rep, agavero, _1800_coconut, corralejo_rep, arette]

def main():
    for item in products:
        for lookup in item['stores']:
            shop_name, price = lookup
            if price == False:
                print("{} is out of stock, unfortunately.".format(item['name']))
            elif price <= item['p_price']:
                print("{} has {} on sale for {}.".format(shop_name,item['name'],price))




if __name__ =='__main__':
    main()














'''
class product(object):
    def __init__(self, name, preferred_price, places):
        self.name = name
        self.p_price = preferred_price
        self.places = places

class shop(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
'''
