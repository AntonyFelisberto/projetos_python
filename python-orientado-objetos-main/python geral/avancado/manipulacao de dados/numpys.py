#pip install numpy
import numpy as np 
arr = np.array([1,2,3,4,5])
arr = np.array([[1,2,3],[10,20,30]]) # 2-Dimensional Array
arr = np.random.randint(10, size=(3, 5, 6)) # create 3 arrays with 5 rows and 6 columns each.
arr = np.empty([2,3]) # creates 2D array  with 2 rows, 3 columns
arr0 = np.zeros(2) # creates a 1D array with 2 elements whose value is 0.
arr1 = np.ones(2) # creates a 1D array with 2 elements whose value is 1
arr2 = np.asarray([1,2,3]) # creates a 1D array with 3 elements
arr3 = np.random.rand(2,3) # creates an array with 2 rows and 3 columns by using random module for uniformly distributed numbers

arr = [1,2]
np.append(arr, [3,4,5]) #adds 3,4,5 at the end and gives result as [1,2,3,4,5]

np.delete([1,2,3,4,5], 4) #removes 4 from the array and gives result as [1,2,3,5]

arr = np.sort([[5,3,1],[7,4,5]], axis=1, kind = 'quicksort')
# gives results as [[1 3 5]
# [4 5 7]]

x = [1,2,3]
y = [4,5,6]
z = [x,y]
np.concatenate(z)# gives result as: [1 2 3 4]
