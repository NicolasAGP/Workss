from unittest import result
import urllib.request
import unittest
from unittest import TestCase
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

URL_BASE = 'http://books.toscrape.com/'
urll = []
class AddRemoveElements(unittest.TestCase):
	def setUp(self):
		self.datos = urllib.request.urlopen('http://books.toscrape.com/').read().decode()

	def test_search_ps4(self):
		for i in range(1, 10):

			if i > 1:
				dats = "%s/catalogue/page-%d.html" % (self.datos, i)
				r = requests.get(dats)
            	soup =  BeautifulSoup(r.text, 'html.parser')					
			else:
				print('pass')
	def ss(self):
				

		

if __name__ == "__main__":
   	unittest.main(verbosity = 2)
