def insertSort(arr=None):
	#nothing done yet
	for i in range(1, len(arr)):
		k = i #start at index 1 instead of 0 since index 0 will not be compared with anything before it
		while(k > 0): #iterates through all the values before it
			buf = 0
			if(arr[k-1] > arr[k]): #swap the values if the one before is larger than the one after
				buf = arr[k-1]
				arr[k-1] = arr[k]
				arr[k] = buf
			k = k - 1 #iterates through all the valus before the one we are starting with
	
	print("\nAfter sorted:")
	print(arr)
	return

def main():
	f = open("data.txt", "r")
	stringData = f.readline().split() #Reads in the line from the data.txt file and splits it into an array based on the spaces between numbers
	newArr = [int(stringData[i]) for i in range(1, int(stringData[0]) + 1)] #Creates a new array that turns the strings to numbers
	print("Before sorted:")
	print(newArr)

	insertSort(newArr)

main()
