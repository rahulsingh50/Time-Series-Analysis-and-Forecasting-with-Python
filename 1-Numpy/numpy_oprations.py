'''

Numpy code 
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


