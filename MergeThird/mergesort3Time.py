import random
import time

#NOTE: most of the documentation is done in the mergesort3 program as this is just an extension of the mergesort3 program
#function merges the split up array sorting it on the way
def merge(arr, left, middle, right):
	i = 0
	j = 0
	h = 0
	k = 0

	#Gets the min value from all three arrays
	while(i < len(left) and j < len(right) and h < len(middle)):
		if(left[i] <= right[j] and left[i] <= middle[h]):
			arr[k] = left[i]
			i = i + 1
		elif(right[j] <= left[i] and right[j] <= middle[h]):
			arr[k] = right[j]
			j = j + 1
		elif(middle[h] <= left[i] and middle[h] <= right[j]):
			arr[k] = middle[h]
			h = h + 1
		else:
			print(left[i])
			print(middle[h])
			print(right[j])
			return
		k = k + 1
	

	#Gets the min values from the two arrays with remaining values
	while(i < len(left) and j < len(right)):
		if(left[i] < right[j]):
			arr[k] = left[i]
			i = i + 1
		else:
			arr[k] = right[j]
			j = j + 1
		k = k + 1

	while(j < len(right) and h < len(middle)):
		if(right[j] < middle[h]):
			arr[k] = right[j]
			j = j + 1
		else:
			arr[k] = middle[h]
			h = h + 1
		k = k + 1

	while(h < len(middle) and i < len(left)):
		if(middle[h] < left[i]):
			arr[k] = middle[h]
			h = h + 1
		else:
			arr[k] = left[i]
			i = i + 1
		k = k + 1


	#Gets the values from the array with the remaining values
	while(i < len(left)):
		arr[k] = left[i]
		i = i + 1
		k = k + 1

	while(j < len(right)):
		arr[k] = right[j]
		j = j + 1
		k = k + 1

	while(h < len(middle)):
		arr[k] = middle[h]
		h = h + 1
		k = k + 1
	
	return


#Function recursivly splits an array until they are single length arrays
#After the array is split up it will be merged back together and ordered least to greatest
#Function takes in an array to sort
def mergeSortThird(arr):
	arrLen = len(arr)
	
	if(arrLen <= 1): #returns when its just a single element
		return

	#Creates the three indexes for the three parts of the array
	third = int(arrLen/3)
	tThird = 2 * third

	#If the origional array is not cleanly broken into three parts then make the first and second if needed bigger
	if(arrLen % 3 == 1):
		third = third + 1
	elif(arrLen % 3 == 2):
		tThird = tThird + 1

	#Creates the three arrs
	left = arr[:third]
	middle = arr[third:tThird]
	right = arr[tThird:]

	mergeSortThird(left)#recursivly splits the left side first
	mergeSortThird(middle)#recursivly splits the middle side
	mergeSortThird(right)#recursivly splits the right side

	merge(arr, left, right, middle)#Finally merges it all back into the arr

	return

#Function that creats a random array given a size n of values ranging from 0 - 10,000
#Takes in the size of an array to create and returns the array of random values
def randomArr(n):
	arr = [None] * n
	for i in range(0, n):
		arr[i] = random.randrange(10001)

	return arr
	
def main():
	random.seed()#seeds the random number generator

	testArr = randomArr(10)

	#Loop that runs through 10 values of n, sorting each array, and printing the time it took along with the size of the array
	n = 50000
	for i in range(0, 10):
		curTime = time.clock()
		testArr = randomArr(n)
		mergeSortThird(testArr)
		print(n, (time.clock() - curTime))
		n = n + 50000

main()
