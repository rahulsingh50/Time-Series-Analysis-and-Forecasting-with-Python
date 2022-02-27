'''

This is Numpy code 
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
