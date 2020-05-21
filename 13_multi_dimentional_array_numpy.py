from numpy import *

arr = array([
            [1, 2, 3, 4, 9, 10],
            [5, 6, 7, 8, 11, 12]
            ])
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
# convert two daimnetional array to single
arr1 = arr.flatten()
print(arr1)
arr2 = arr1.reshape(3, 4)
print(arr2)

arr2 = arr1.reshape(2, 2, 3)
print(arr2)

m = matrix('1, 2, 3 ; 4, 5, 6 ; 7, 8, 9')
print(m)
print(diagonal(m))
print(m.min())
print(m.max())
print(m.sum())
print('##################################')
m1 = matrix('1, 2, 3 ; 4, 5, 6 ; 7, 8, 9')
m2 = matrix('1, 4, 3 ; 4, 2, 6 ; 5, 9, 2')

m3 = m1 + m2
print(m3)
m3 = m1 * m2
print(m3)






