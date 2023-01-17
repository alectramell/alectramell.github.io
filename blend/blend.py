import random

def clear():

	import os
	import platform
	OSname = str(platform.system())

	if OSname == 'Windows':
		os.system('cls')

	else:
		os.system('clear')

class blend:

	def file(xfile):

		zfile = open(f'{xfile}','r')
		zdata = zfile.read()
		zfile.close()

		mixdata = list(zdata.strip().replace(' ',''))
		random.shuffle(mixdata)
		xout = str(''.join(mixdata))

		return(xout)

	def text(zdata):

		mixdata = list(zdata.strip().replace(' ',''))
		random.shuffle(mixdata)
		xout = str(''.join(mixdata))

		return(xout)

	def help():

		clear()

		xinfo = '''
BLEND v1.0 | Python 3 Module

Usage:

From String..

	>> from blend import *
	>> xword = blend.text('word')
	>> print(xword)

From File..

	>> from blend import *
	>> xfile = blend.file('file.txt')
	>> print(xfile)'''

		print(xinfo)