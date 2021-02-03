import random
import time

#
#This function takes in the item array, the max capacity of the bag, and the number of items
#This function returns the max value that can be held with the given items and capacity
def buildTable(itemArr=None, capacity=None, itemNum=None):
	#The initialization of the array below was gotten from StackOverflow
	#https://stackoverflow.com/questions/21036140/python-two-dimensional-array-changing-an-element
	#I was having troubles initializing the 2D array by using [[0] * n] * W as it was duplicating the same inner array instead of initializing new ones
	vArr = [[0] * (capacity+1) for _ in range(0, itemNum+1)]
	
	#Fills in each part of the array except for the first line which is filled with 0s (base case)
	for i in range(1, itemNum+1):
		for j in range(1, capacity+1):
			curWeight = itemArr[i-1][0]
			curVal = itemArr[i-1][1]
			
			#Checks to see if current item weight can fit in given capacity
			if curWeight <= j:
				#Check to see if adding current items value is better option than previous cption
				if(curVal + vArr[i-1][j-curWeight] > vArr[i-1][j]):
					vArr[i][j] = curVal + vArr[i-1][j-curWeight]#If so add new combintion value to value table
				else:
					vArr[i][j] = vArr[i-1][j]#Otherwise use pervious option
			else:#If item cant even fit in current capacity then use previous option
				vArr[i][j] = vArr[i-1][j]

	#Return the max value that can be acheived
	return vArr[i][j]


#This function is the recursive version of this knapsack problem
#Takes in the capacity, the item being looked at, and the item array
def knapsack(capacity, item, itemsArr=None):
	if(capacity == 0 or item == 0):#Base case which is when the capacity or item number reaches 0
		return 0

	curWeight = itemsArr[item-1][0]
	curVal = itemsArr[item-1][1]

	#IF item is too big for current capacity then use check the item before this
	if(curWeight > capacity):
		return knapsack(capacity, item-1, itemsArr)
	#otherwise return the max between the new combination with the current item or the previous combination with the item before
	else:
		return max((curVal + knapsack(capacity - curWeight, item-1, itemsArr)), knapsack(capacity, item-1, itemsArr))


#Function creats the item array that is used by the programs to fill the bag to acheive maximum value
#Takes in the length of the item array
#Returns the 2D item array with the weight in the first part and the value inthe second index
def createItemArray(itemNum):
	items = []

	for i in range(0, itemNum):
		#Creats an array where first value is the weight and the second is its value
		weightVals = [None] * 2
		weightVals[0] = random.randrange(60) + 5 #Weight is randomly set 5-64. Wanted to minimum weight not to be too small and the max not to be too big
		weightVals[1] = random.randrange(100) + 10#Doesnt really matter what the value is set at
		items.append(weightVals)

	return items


#Function was used for error handling to see if the value table I had matched with my expected results
#Used this to test the case that was demonstrated in class
def printArr(arr, leng, widt):
	for i in range(0, widt+1):
		for j in range(0, leng+1):
			print(arr[j][i]),
		print("\n")

	return

def main():
	random.seed()#seeds the random number generator
	
	capacity = 100
	itemsNum = 35
	#itArr = [[2, 3], [3, 4], [4, 5], [5, 6], [5, 8]]

	for i in range(0, 10):
		curTime = time.process_time()
		itArr = createItemArray(itemsNum)
		maxRec = knapsack(capacity, itemsNum, itArr)
		
		#This formating technique was gotten from the Loyola University of Chicago website on python documentation
		#http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/float.html
		#I was having weird problems with the times coming out at only one decimal place so I switch to python 3.4 and used process_time() instead
		#I used the format documentation to only show 4 decimal places
		recTime = format(time.process_time() - curTime, '.4f')
		print("N=" + str(itemsNum) + " W=" + str(capacity) + " Rec time = " + str(recTime), end=' ')
		curTime = time.process_time()
		maxDP = buildTable(itArr, capacity, itemsNum)
		dpTime = format(time.process_time() - curTime, '.4f')
		print("DP time = " + str(dpTime) + " max Rec " + str(maxRec) + " max DP = " + str(maxDP))
		capacity = capacity + 25
	return	

main()
