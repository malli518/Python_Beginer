import array as arr
val = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
print(val.typecode)
print(val.buffer_info())
val.reverse()
print(val)
for i in val:
    print(i)

# char array
char = arr.array('b', [ord('g'), ord('e'), ord('e'), ord('k')])
for i in char:
    print(i)

# new array with exiting array values
newArr = arr.array(val.typecode, (a for a in val))
i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1

