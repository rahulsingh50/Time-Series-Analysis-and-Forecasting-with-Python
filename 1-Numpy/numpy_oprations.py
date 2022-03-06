'''

Numpy code 
Sypder Short cut
Run - FN + F9
Function Argument - Ctr+ i

'''

import numpy as np

numpy_2d_array1 = np.array([[1,2],[4,5]])

# Normal Element Multipilcation Vs Matrix Multiplication

numpy_2d_array2 = np.array([[5,6],[2,3]])

element_arr_mul = numpy_2d_array1 * numpy_2d_array2
matrix_mul = numpy_2d_array1@numpy_2d_array1

# using the class perform matrix multiplication and element to element multiplication

mtx_mul = np.dot(numpy_2d_array1,numpy_2d_array2)
element_arr_mul2 = np.multiply(numpy_2d_array1,numpy_2d_array2)


# Array and Matrix Subtraction and Addition

arr_add1 = numpy_2d_array1 + numpy_2d_array2
arr_sub1 = numpy_2d_array1 - numpy_2d_array2

# using class method

arr_add2 = np.add(numpy_2d_array1, numpy_2d_array2)
arr_sub2 = np.subtract(numpy_2d_array1, numpy_2d_array2)

# adding Element of array

arr_sum = np.sum(numpy_2d_array1)

# Brocasting of array
# boradcasting the means performing the opration make the same size array and matrix


brod_add = numpy_2d_array1 +3 

numpy_array3 = np.array([1,2])

broad_add = numpy_2d_array1 + numpy_array3


# Division 

division = np.divide([1,2,4,6],6)
division2 = np.floor_divide([12,3,45],5)

# mathmatical fuctions

squar_fuanction = np.math.sqrt(5)


# Random distribution
sd_normal_data = np.random.standard_normal(100)
# standerd normal data 3 row and 1 colum (mean = 0 and SD = 1) or array
sd_normal_arr = np.random.standard_normal((3,2))
# low = 0 and high 1 and size give to number of sample called uniform data
uni_ds = np.random.uniform(1,3,10)

# array of uniform distribution
uni_ds_array = np.random.uniform(1,5,(2,3))


# random number flot ,low ,high and size
rf_arr = np.random.rand()

#  random number intiger ,low,high and size

rf_int = np.random.randint(2,10,[4,5])


# zero

zero = np.zeros((2,3))
one = np.one((2,3))

# Filter Array

random_arr = np.random.randint(1,50,(2,5))

# logical and condition
tf_random_arr = np.logical_and(random_arr >30,random_arr < 50)
fiter_rand_arr = random_arr[tf_random_arr]

# Statistics 

arr_1d = np.array([1,2,4,5,7])

# mean sum(n)/n
mean_1d = np.mean(arr_1d)
# variance sum(n- mean)/n
var_1d = np.var(arr_1d)

# standeerd deviation
# squreroot(sum(n-mean)/n)
sd_1d = np.std(arr_1d)

# median - sorting asending middle value
mean_1d = np.median(arr_1d)

# mode most comman value,possibel more than one

# 2d array 
arr_2d = np.array([[1,2,5],[4,5,6]]) 

var_rowwise= np.var(arr_2d, axis=1)
var_col= np.var(arr_2d,axis = 0)
   
    
    



