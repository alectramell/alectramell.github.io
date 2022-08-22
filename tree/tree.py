import os
import sys
import hashlib
import binascii
import platform
import webbrowser

def clear():

	if str(platform.system()) == 'Windows':

		import os
		os.system('cls')

	else:

		import os
		os.system('clear')

def md5(xvar):

	import hashlib
	yvar = hashlib.md5(xvar.encode())
	return(yvar.hexdigest())

def hex(xvar):

	import binascii
	yvar = bytes(xvar, encoding='utf-8')
	zvar = binascii.hexlify(yvar)
	return(zvar.decode())

def unhex(xvar):

	import binascii
	yvar = str(xvar)
	zvar = binascii.unhexlify(yvar)
	return(zvar.decode())

class tree:

	global sdata
	sdata = str('savedata')

	def save(xname, xdata):

		if os.path.exists(f'{sdata}'):

			pass

		else:

			os.mkdir(f'{sdata}')

		xname = str(md5(xname.lower()))
		xdata = str(hex(xdata))
		xfile = open(f'{sdata}/{xname}.tree','w')
		xfile.write(f'{xdata}')
		xfile.close()

	def load(xname):

		xname = str(md5(xname.lower()))
		xfile = open(f'{sdata}/{xname}.tree','r')
		xdata = str(unhex(xfile.read()))
		xfile.close()
		return xdata

	def kill(xname):

		xname = str(md5(xname.lower()))
		xfile = str(f'{sdata}/{xname}.tree')

		if os.path.exists(xfile):

			os.remove(xfile)

		else:

			pass

	def help():

		xurl = str('https://alectramell.github.io/tree')
		webbrowser.open_new(xurl)