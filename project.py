from unittest import result
import urllib.request
import unittest
from unittest import TestCase
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

URL_BASE = 'http://books.toscrape.com/'
MAX_PAGES = 51
counter = 0
productlist = []


class AddRemoveElements(unittest.TestCase):
    for i in range(1, MAX_PAGES):
    # Construyo la URL
        if i > 1:

            url = "%s/catalogue/page-%d.html" % (URL_BASE, i)

        else:
            url = URL_BASE
        def get_data(url):
            r = requests.get(url)
            soup =  BeautifulSoup(r.text, 'html.parser')

            return soup


        def parse(soup):


            listaa=[]
            results = soup.find_all('article', {'class': 'product_pod'})
            for item in results:


                products = {
                    'title': item.find('a'),

                    'Price': (item.find('p', {'class':'price_color'}).text.replace('£','').replace(',','').replace('Â','').strip()),
                }
                productlist.append( products)

            return productlist

        def output(productlist):
            productsdf = pd.DataFrame(productlist)
            productsdf.to_csv('libros_url.csv', index=False)
            return

        soup = get_data(url)
        productlist = parse(soup)
        output(productlist)
if __name__ == "__main__":
    unittest.main(verbosity = 2)
