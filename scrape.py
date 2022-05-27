import os
import sys
import requests

class scrape:

	def data(xurl, xtag):

		# xurl is website url, ie 'https://alectramell.github.io'
		# xtag is html tag to extract, ie '<title>'

		html = requests.get(xurl)
		page = html.text

		p1 = page.find('<'+xtag+'>')
		p2 = p1 + len('<'+xtag+'>')
		p3 = page.find('</'+xtag+'>')
		return page[p2:p3].strip()

xout = scrape.data('https://www.google.com','title')
os.system('cls')
print(xout+' is a search engine..')