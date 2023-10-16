import os
import sys
import hashlib
import platform

def clear():
	if str(platform.system()).lower() == 'windows':
		os.system('cls')
	else:
		os.system('clear')

def md5(xvar):
	import hashlib
	yvar = hashlib.md5(xvar.encode())
	return(yvar.hexdigest())

class hex:

	def enc(xvar):
		xvar = str(xvar)
		xdat = xvar.encode().hex()
		return xdat

	def dec(svar):
		svar = str(svar)
		sdat = bytes.fromhex(svar).decode('utf-8')
		return sdat