import os
import sys
import urllib.request

# Updated 2022

class wifi:

	def connected():

		try:
			urllib.request.urlopen('https://alectramell.github.io')
			return(True)
		except:
			return(False)