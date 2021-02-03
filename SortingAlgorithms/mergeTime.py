import random
import time

#merge function
#this takes in three arrays, the main one and the two split up ones to merge back to the main
def merge(arr, left, right):
	i = 0
	j = 0
	k = 0

	#After done splitting this seciton will merge and sort
	while(i < len(left) and j < len(right)):
		if(left[i] < right[j]):
			arr[k] = left[i]
			i = i + 1
		else:
			arr[k] = right[j]
			j = j + 1
		k = k + 1

	#if there are anny values left in either of the arrays then add them to the end of the merged array
	#note that since we are merging already merged/sorted arrays that adding the element to the end will not mess up the order
	#This will only happen if the array has an odd number of elements
	while(i < len(left)):
		arr[k] = left[i]
		i = i + 1
		k = k + 1

	while(j < len(right)):
		arr[k] = right[j]
		j = j + 1
		k = k + 1


	return

#mergeSort function
#Takes in an array and recursively splits it until it is a single element
#After split, it is merged back together and sorted while doing so 
def mergeSort(arr):
	if(len(arr) <= 1): #stop splitting the array when it is one element
		return

	middle = int(len(arr)/2) #get the middle point to split the origional array by
	

	left = arr[:middle] #creates left and right array from midpoint
	right = arr[middle:]

	#recursive call for this new split array
	mergeSort(left)
	mergeSort(right)
	merge(arr, left, right)
	
	return

#function creates an array of size n and fills it with a random number from 0 - 10000
#returns said array
def createRanArray(n):
	randArr = [None] * n
	for i in range(0, n):
		randArr[i] = random.randrange(10001)

	return randArr

def main():
	random.seed()
	mergeSortTimes = [None] * 10 #array to hold the times of the different size n
	
	curTime = 0 #variable to measure the time it takes for the algorithm to run
	n = 100000

	tempArr = createRanArray(100)
	print(tempArr)
	mergeSort(tempArr)
	print(tempArr)

	#does all the time calculations in one loop 
	for i in range(0, 10):
		curTime = time.clock()
		tempArr = createRanArray(n)
		mergeSort(tempArr)
		mergeSortTimes[i] = (time.clock() - curTime)
		print(n, mergeSortTimes[i])
		n = n + 50000

main()
