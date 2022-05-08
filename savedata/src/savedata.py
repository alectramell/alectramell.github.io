import os
import sys
import hashlib
import binascii
from threading import Thread

homepath = str(os.getcwd())
datapath = str(f'{homepath}/savedata/')
datastatus = os.path.isdir(datapath)

if datastatus == False:

	os.mkdir(datapath)

else:

	pass

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

class data:

	def save(zfile, zdata):

		filename = str('savedata/')+str(md5(zfile))
		ydata = hex(zdata)
		xdata = str(ydata)[::-1]

		xfile = open(filename, 'w')
		xfile.write(xdata)
		xfile.close()

	def load(zfile):

		filename = str('savedata/')+str(md5(zfile))

		try:

			xfile = open(filename, 'r')
			xdata = xfile.read()
			xfile.close()

			ydata = str(xdata)[::-1]
			zdata = str(unhex(ydata))

			return(zdata)

		except:

			return('0')

