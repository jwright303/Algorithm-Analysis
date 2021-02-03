import random
import sys

#Function that goes through the value table and find the items that were added to the cart
#Function takes in the value table to search through, the number of items in the table, the max weight to look for and the item array
#This function returns a cart with the total value the person can carray as well as the items that they would carry
def findItems(vArr, itemNum, maxW, itemArr):
	cart = []
	#First adds the value of all the things they can carry
	cart.append(vArr[itemNum][maxW])
	i = itemNum
	j = maxW

	#Then iterates through to see which items they would need to cary to reach the max value
	while(i > 0 and j > 0):
		#This essentially checks to see if the previous answer was used in this slot and if it wasnt then the item was used
		if(vArr[i][j] != vArr[i-1][j]):
			cart.append(i)
			i = i - 1
			j = j - itemArr[i][1]
			#print(j)
		#Otherwise move on to the next slot
		else:
			i = i - 1

	return cart


#Function fills in the value table, if its partially full then it adds to what is already there
#This function takes in the value table to fill, the item array, the max capacity, and the maximum capcity the table has already been filled to
#This funciton returns the list of items and their total value by calling the findItems function
def fillValTable(vArr, itemArr, capacity, largW):
	itemNum = len(itemArr)
	startW = 1

	#Sets the starting point to where it was left off +1 or just 1 if it is empty
	if largW == 0:
		startW = 1
	else:
		startW = largW+1
	
	#Starts filling in the value table
	for i in range(1, itemNum+1):
		for j in range(startW, capacity+1):
			curWeight = itemArr[i-1][1]
			curVal = itemArr[i-1][0]
			if curWeight <= j:#If the item can fit in the given capacity then see if adding its value helps
				#If adding this with a pervious item is better then mark it down in the table otherwise use pervious value
				if(curVal + vArr[i-1][j-curWeight] > vArr[i-1][j]):
					vArr[i][j] = curVal + vArr[i-1][j-curWeight]
				else:
					vArr[i][j] = vArr[i-1][j]
			else:#If item too big then use previous solution
				vArr[i][j] = vArr[i-1][j]

	#Find the items that gave this max value and return them as an array
	return findItems(vArr, i, capacity, itemArr)


#This function prints out the cart of the entire family in the format that was show on the assignment page
#Takes in the cart which is a 2D array as well as the test case number
#Returns nothing, instead prints out to the screen which as mentioned earlier has been redirected to a file
def printTestCase(familiesCart, testCase):
	cartSum = 0
	#First sums all the members carts which is contained in the first element of their cart 
	for i in range(0, len(familiesCart)):
		cartSum = cartSum + familiesCart[i][0]

	print("Test case: " + str(testCase))
	print("Total price: " + str(cartSum))
	print("Member Items")

	#Now iterates through each family member and their given cart
	for i in range(0, len(familiesCart)):
		#print(str(i+1) + ": ", end="")
		print(str(i+1) + ": "),
		for j in range(1, len(familiesCart[i])):
			#print(str(familiesCart[i][j]), end=" "),
			print(str(familiesCart[i][j])),
		print("")
	return

#Same printing function that was used in knapsack problem to help debug
def printArr(arr, leng, widt):
	for i in range(0, widt+1):
		for j in range(0, leng+1):
			print(arr[j][i]),
		print("\n")

	return

#Main Function
def main():
	f = open("shopping.txt", "r")#opens the file to read the test cases from
	testCases = int(f.readline())#Gets the number of test cases
	#The redirection of stdout to a file was gotten form stackoverflow:
	#https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python
	sys.stdout = open('results.txt', 'w')

	#Iterates through each test case
	for h in range(0, testCases):
		largestWeight = 0 #starts off with the biggest capacity written to the table being 0
		#Initializes the value table. As states by the assignment the number of items is <= 100 and the capacity of a family member is <= 200
		valArr = [[0] * (201) for _ in range(0, 101)]
		cartArr = []
		itArr = []
		capArr = []
		items = int(f.readline())

		#Given the number of items, this iterates through, creates an array of price and weight then adds this to item array
		for i in range(0, items):
			strData = f.readline().split() #First split by spaces, then convert to ints below
			itArr.append([int(strData[i]) for i in range(0, len(strData))])
		
		famNum = int(f.readline())
	
		#For the number of family members, add the maximum they can carry to the capacity array
		for i in range(0, famNum):
			capacity = int(f.readline())
			capArr.append(capacity)
		
		#Finally for each family member get the max value they can carry and its corresponding items
		for i in range(0, famNum):
			newItem = []

			#If the current capacity is less than or equal to the largest capacity built into the table then just search for the items
			if capArr[i] <= largestWeight:
				newItem = findItems(valArr, items, capArr[i], itArr)
			#Otherwise fill in the able. This can continue from where its left off by giving its the largestWeight that it has filled in
			else:
				newItem = fillValTable(valArr, itArr, capArr[i], largestWeight)
			
			#These lists of items are added to the families cart
			cartArr.append(newItem)
			#If this family members carry capacity is bigger than the pervious biggest then update it
			if capArr[i] > largestWeight:
				largestWeight = capArr[i]
		
		#Prints out the test case in a specific format
		#printArr(valArr, largestWeight, items)
		printTestCase(cartArr, h+1)
		print("")

	f.close()
	return	

main()
