# Arrays

def arrays(arr):
    return (numpy.array(arr[::-1], float))

# Shape and Reshape

import numpy
array_1d = list(map(int, input().split()))
print(numpy.reshape(array_1d, (3,3)))

# Transpose and Flatten 

import numpy
rows, columns = map(int,input().split())
array = []
for _ in range(rows):
    array.append(list(map(int, input().split())))
my_array = numpy.array(array)
print(numpy.transpose(my_array))
print(my_array.flatten())

# Concatenate

import numpy
n, m, p = map(int, input().split())
array1 = numpy.array([input().split() for _ in range(n)],int)
array2 = numpy.array([input().split() for _ in range(m)],int)
print(numpy.concatenate((array1, array2), axis = 0))

# Zeros and Ones

import numpy
*v, = map(int, input().split())
print(numpy.zeros(v, dtype = numpy.int))
print(numpy.ones(v, dtype = numpy.int))

# Eye and Identity

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1', ' 1').replace('0', ' 0'))

# Array mathematics 

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')

# Floor, Ceil and Rint

import numpy
numpy.set_printoptions(sign = ' ') # required for the validation of solutions

nums = list(map(float, input().split()))
arr = numpy.array(nums)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

# Sum and Prod

import numpy
rows, cols = map(int,input().split())
arrp = []
for _ in range(rows):
    arrp.append(list(map(int, input().split())))
my_arr = numpy.array(arrp)
print(numpy.prod(numpy.sum(my_arr, axis = 0)))

# Min and Max

import numpy
rows, cols = map(int,input().split())
arrp = []
for _ in range(rows):
    arrp.append(list(map(int, input().split())))
my_arr = numpy.array(arrp)
print(numpy.prod(numpy.sum(my_arr, axis = 0)))

# Mean, Variance and Standard Deviation

import numpy
numpy.set_printoptions(legacy='1.13') # default to a older version of the numpy module

rows, cols = map(int,input().split())
arrp = []
for _ in range(rows):
    arrp.append(list(map(int, input().split())))
my_arr = numpy.array(arrp)
print(numpy.mean(my_arr, axis = 1))
print(numpy.var(my_arr, axis = 0))
print(numpy.std(my_arr, axis = None))

# Dot and Cross

import numpy
rows = int(input())
x = [] 
y = []
for _ in range(rows):
    x.append(list(map(int, input().split())))
a = numpy.array(x)
for _ in range(rows):
    y.append(list(map(int, input().split())))
b = numpy.array(y)
print(numpy.dot(a,b))

# Inner and Outer 

import numpy
a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))
print(numpy.inner(a,b))
print(numpy.outer(a,b))

# Polynomials

import numpy
coefficients = list(map(float, input().split()))
x = int(input())
print(numpy.polyval(coefficients, x))

# Linear Algebra

from numpy import linalg
det = []
for _ in range(int(input())):
    v = list(map(float, input().split()))
    det.append(v)
print(round(linalg.det(det), 2))


