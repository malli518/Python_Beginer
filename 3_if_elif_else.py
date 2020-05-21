# x=input('Enter a number')
# y=input('Enter a number')
# print x+y
x = int(input('Enter a number'))
r = x % 2
if r == 0:
    print('Even')
    if 5 < x < 10:
        print('Great')
    elif x > 10:
        print('Super Great')
    else:
        print('Not Great')
else:
    print('Odd')
print('bye')
