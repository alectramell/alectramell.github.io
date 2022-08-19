import os
import sys

def pair(xfunc, yfunc):

	from multiprocessing import Process

	if __name__ == "__main__":

		function1 = Process(target=xfunc)
		function2 = Process(target=yfunc)

		function1.start()
		function2.start()

		function1.join()
		function2.join()

# Usage..
#
# from pairing import *
#
# >>> pair(function1(), function2())