import os
import sys
import math
testlist = [[91207, 89566], [-88690, -83026], [67100, 47194]]

def run():
	middley = findmiddle(testlist)
	print middley


def findmiddle(testlist):
	ylist = []
	for x in testlist:
		ylist.append(x[1])
	ymin = min(ylist)
	ylist.remove(ymin)
	ymin2 = min(ylist)
	return ymin2 

if __name__ == "__main__":
	run()
