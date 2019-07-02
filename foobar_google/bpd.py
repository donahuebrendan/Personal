import os
import sys
import math
def run():
	coinin = int(sys.argv[1])
	guazlist = [coinin]
	squarelist = square()
	outlist = []
	while True:
		length = len(guazlist)
		closestout = closesquare(guazlist[length-1])
		guazlist.append(closestout)
		outlist.append(math.sqrt(guazlist[length-1]-closestout))
		if closestout in squarelist:
			outlist.append(math.sqrt(closestout))
			print outlist
			output = len(outlist)
			print ("the amount of guaz pads is: " + str(output))
			break
def closesquare(coins):
	for x in range(100):
		square = x*x
		temp = int(coins) - square
		if temp < 0:
			closesquare = x-1
			print ("closest square is: " + str(closesquare))
			stepdown = coins - (closesquare * closesquare)
			break
	return stepdown
def square():
	slist = []
	for x in range(100):
		slist.append(x*x)
	return slist
if __name__ == "__main__":
	run()
