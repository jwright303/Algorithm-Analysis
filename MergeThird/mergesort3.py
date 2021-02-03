import random

#function merges the split up array sorting it on the way
#For this merge function we have three rounds of merging
#The first round of merging is for when all the 3 parts have values that haven't been checked yet
#Second round is for merging when 2 parts still have values to check
#The last round is for when one part has unchecked values and these are added to the end of the array
#arr is the origional array that the three parts were made from and its values are replaced with the smallest of the 3 parts as it iterates
def merge(arr, left, middle, right):
	i = 0
	j = 0
	h = 0
	k = 0

	#Gets the min value from all three arrays
	#Each time a value is taken from one of the parts that parts incraments its index
	while(i < len(left) and j < len(right) and h < len(middle)):
		if(left[i] <= right[j] and left[i] < middle[h]):
			arr[k] = left[i]
			i = i + 1
		elif(right[j] < left[i] and right[j] <= middle[h]):
			arr[k] = right[j]
			j = j + 1
		elif(middle[h] <= left[i] and middle[h] <= right[j]):#last case should be less than or equal on the odd chance 3 of the same values are compared
			arr[k] = middle[h]
			h = h + 1
		else: #shouldnt ever run this part, this was just for error checking
			print(left[i])
			print(middle[h])
			print(right[j])
			return
		k = k + 1
	

	#Gets the min values from the two arrays with remaining values
	#This part was the same as the normal merge function except there are three since need to check all 2 combinations of the 3 parts
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


	#Values from the array with the remaining values
	#At this point only one array 
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


def mergeSort(arr):
	arrLen = len(arr)
	
	if(arrLen <= 1): #returns when its just a single element
		return

	third = int(arrLen/3)#Ceates the index for the first third
	tThird = 2 * third#Creates the index for the second/last third

	if(arrLen % 3 == 1):#If odd number of parts make the first the biggest
		third = third + 1
	elif(arrLen % 3 == 2):#If odd number of parts make the first two the bigger ones
		tThird = tThird + 1

	#creates arrays for the three parts
	left = arr[:third]
	middle = arr[third:tThird]
	right = arr[tThird:]

	mergeSort(left)#recursivly splits the left third
	mergeSort(middle)#recursivly splits the middle third
	mergeSort(right)#recursivly splits the right third

	merge(arr, left, right, middle)#finally merge all of the parts back to the origional arr

	return


def main():
	fileToSort = open("data.txt", "r")#opens the file

	for line in fileToSort:#This time gets each line from the file, parses it into an array, and then sorts it with mergesort
		stringData = line.split()#splits the line by spaces so each number is now stored as a string in an array
		newArr = [int(stringData[i]) for i in range(1, int(stringData[0]) + 1)]#converts to a new array of ints instead of strings
		#print(newArr)
		mergeSort(newArr)
		print(newArr)
		#print("\n")

	fileToSort.close()#finally close the file

main()
