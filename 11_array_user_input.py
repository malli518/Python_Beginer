import array as arr

val = arr.array('i', [])

n = int(input('Enter the size of array'))

for i in range(n):
    x = int(input('enter the value'))
    val.append(x)

print(val)

e = int(input('enter a value to search'))
k = 0
for j in val:
    if e == j:
        print(k)
        break
    k += 1
print(val.index(e))

