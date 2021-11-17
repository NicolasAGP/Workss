from unittest import result
import urllib.request
import unittest
from unittest import TestCase
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

class AddRemoveElements(unittest.TestCase):
	def setUp(self):
		self.datos = urllib.request.urlopen('http://books.toscrape.com/').read().decode()

	def test_search_ps4(self):
		datos = self.datos
		soup =  BeautifulSoup(datos)
		tags = soup('a')
		urll = []
		for tag in tags:
			urll.append(tag.get('href'))
		df = pd.DataFrame({'url': urll})
		df.to_csv('libros_url.csv')

if __name__ == "__main__":
    unittest.main(verbosity = 2)
