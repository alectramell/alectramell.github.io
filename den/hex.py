import os
import sys

class hex:

	def enc(xvar):

		xvar = str(xvar)
		xdat = xvar.encode().hex()
		return xdat

	def dec(svar):

		svar = str(svar)
		sdat = bytes.fromhex(svar).decode('utf-8')
		return sdat