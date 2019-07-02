import os
import sys
def run():
	testcase2 = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
	testcase1 = [[5, 1, 5], [10, 1 ,2]]
	answer(testcase2)
	print "***************************"
	answer(testcase1)
	
def answer(listoflist):
	listlen = len(listoflist)
	count = 0
	ratiolist = []
	for x in listoflist:
		num = float(x[1])
		denom = float(x[2])
		time = float(x[0])
		prob = (num/denom)
		key = time/prob
		print num
		print denom
		print prob
		ratiolist.append([key, count])
		count = count+1
	print ratiolist
	ratiolist = sorted(ratiolist)
	print ratiolist
	outlist = []
	for x in ratiolist:
		print(type(x[1]))
		outlist.append(x[1])
	print "------------------------------"
	print type(outlist)
	print outlist
if __name__ == "__main__":
	run()
