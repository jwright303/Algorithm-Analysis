#documentation and comments for the main and create random array can be found in the mergeTime program

import random
import time

def createRanArray(n):
	randArr = [None] * n
	for i in range(0, n):
		randArr[i] = random.randrange(10001)

	return randArr

#Insert sort function takes in an array and sorts it
#iterates through the array and moves the values up to their propper spot
def insertSort(arr=None):
	for i in range(1, len(arr)):
		k = i #start at index 1 instead of 0 since index 0 will not be compared with anything before it
		while(k > 0): #iterates through all the values before it
			buf = 0
			if(arr[k-1] > arr[k]): #swap the values if the one before is larger than the one after
				buf = arr[k-1]
				arr[k-1] = arr[k]
				arr[k] = buf
			k = k - 1 #iterates through all the valus before the one we are starting with
	return

def main():
	random.seed()
	insertSortTimes = [None] * 10
	
	curTime = 0
	n = 3000
	arrSizes = [5000, 7000, 10000, 12000, 13000, 15000, 17000, 18000]
	tempArr = createRanArray(100)
	print(tempArr)
	insertSort(tempArr)
	print(tempArr)
	
	for i in range(0, 10):
		curTime = time.clock()
		insertSort(createRanArray(n))
		insertSortTimes[i] = (time.clock() - curTime)
		print(n, insertSortTimes[i])
		n = n + 2000
	

main()
