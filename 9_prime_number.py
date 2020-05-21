import math
x = int(input('Enter a number '))
for i in range(2, int(math.sqrt(x) + 1)):
    if x % i == 0:
        print(x, 'Not a prime number')
        break
else:
    print(x, 'Prime number')
