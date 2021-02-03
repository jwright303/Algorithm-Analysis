#NOTE: most of the documentation is done in the mergeTime program. Programs were split up after I finished with all the coding

#function merges the split up array sorting it on the way
def merge(arr, left, right):
	i = 0
	j = 0
	k = 0

	while(i < len(left) and j < len(right)):
		if(left[i] < right[j]):
			arr[k] = left[i]
			i = i + 1
		else:
			arr[k] = right[j]
			j = j + 1
		k = k + 1
	
	#for odd arrays make sure there is no straggler values left behind
	while(i < len(left)):
		arr[k] = left[i]
		i = i + 1
		k = k + 1

	while(j < len(right)):
		arr[k] = right[j]
		j = j + 1
		k = k + 1
	


	return

def mergeSort(arr):
	if(len(arr) <= 1): #returns when its just a single element
		return

	middle = int(len(arr)/2)
	
	left = arr[:middle]
	right = arr[middle:]
	
	mergeSort(left)#recursivly splits the left side first
	mergeSort(right)#recursivly splits the right side

	merge(arr, left, right)
	return
	
def main():
	f = open("data.txt", "r")#same as the insertion sort version
	stringData = f.readline().split()
	newArr = [int(stringData[i]) for i in range(1, int(stringData[0]) + 1)]

	print("Before sort:")
	print(newArr)
	mergeSort(newArr)
	print("\nAfter sort:")
	print(newArr)

main()
