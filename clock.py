import os
import sys
import time

running = True
while running:
	ztime = time.localtime()
	xtime = time.strftime("%I:%M:%S %p", ztime)
	os.system('cls')
	print(xtime)
	time.sleep(0.99)