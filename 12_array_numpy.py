from numpy import *
arr = array([1, 2, 3, 4, 5], float)
print arr
# linspace(starting value, ending value, how may parts you want to split)
# linspace(0,15,16)
# default parts are 50
arr = linspace(0, 15)
print arr

# arange
arr = arange(1, 15, 2)
print arr
# output :: [ 1  3  5  7  9 11 13]

# logspace
arr = logspace(0, 40, 5)
print arr
# output [1.e+00 1.e+10 1.e+20 1.e+30 1.e+40]

# zeros() it will create a array with all zeros
arr = zeros(5, int)
print arr
# output [0 0 0 0 0]

# ones() it will create a array with all ones
arr = ones(5, float)
print arr
# output [1. 1. 1. 1. 1.]


# few more operations on Array

arr = array([1, 2, 3, 4, 5])
arr = arr + 2
print arr
# output [3 4 5 6 7]

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([2, 4, 5, 2, 4])
arr3 = arr1 + arr2

print min(arr1)
print max(arr1)
print sum(arr1)
print concatenate([arr1, arr2])
print arr3


###################################################################
# Shallow copy view() (if you change the value of one array it will reflect to other array as well )
arr = array([1, 2, 3, 4, 5])
arr1 = arr
print arr
print arr1
print id(arr)
print id(arr1)
arr1 = arr.view()
arr[1] = 6
print id(arr1)
print arr1
print arr

print '################################'
# Deep copy (if you change the value of one array it won't reflect to other array as well )
arr = array([1, 2, 3, 4, 5])
arr1 = arr.copy()
arr[1] = 6
print arr
print arr1
print id(arr)
print id(arr1)
