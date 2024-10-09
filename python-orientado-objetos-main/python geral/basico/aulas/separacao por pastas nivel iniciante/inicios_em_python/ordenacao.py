c = 1
a = c
print(a is c)

def buble_sort(arr):
	n = len(arr)
	
	for i in range(n):
		for j in range(0,n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				
	return arr
print(buble_sort([1,2,3,10,9,8,7,6,5,4]))	