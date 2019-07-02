import os
import math
import sys
def answer(coins):
    answerlist = []
    squares = []
    for x in range(int(math.sqrt(float(coins)))):
	print ("attempting: " + str(x))
        firstlist = firsttry(coins, x+1)
        answerlist.append(len(firstlist))
	squares.append(firstlist)
    out = min(answerlist)
    print("-------------------------------")
    print  ("The answer is : " + str(out))	
    number = answerlist.index(out)
    print ("The Answer list was : " + str(squares[number]))
def firsttry(coins, attempt):
        guazlist = [coins]
        squarelist = square()
	if int(coins) in squarelist:
		outlist1 = [math.sqrt(float(coins))]
	else:
        	outlist1 = []
		count = 0
        	while True:
                	length1 = len(guazlist)
                	closestout = closesquare(guazlist[length1-1], (int(attempt)-count))
			if count <= (int(attempt)-2):
				count = count + 1
                	guazlist.append(closestout)
                	outlist1.append(math.sqrt(int(guazlist[length1-1])-int(closestout)))
                	if closestout in squarelist:
                        	outlist1.append(math.sqrt(closestout))
                        	print outlist1
                        	output1 = len(outlist1)
                        	print ("the amount of guaz pads is: " + str(output1))
                        	break
        return outlist1
def closesquare(coins, attempt):
        stepdown = 0
        for x in range(102):
                square = x*x
                temp = int(coins) - square
		if temp < 0:
			closesquare = x-int(attempt)
                        #print ("closest square is: " + str(closesquare))
                        stepdown = int(coins) - (closesquare * closesquare)
			break
        return stepdown
def square():
        slist = []
        for x in range(101):
                slist.append(x*x)
	return slist    # your code here
if __name__ == "__main__":
	answer(sys.argv[1])
