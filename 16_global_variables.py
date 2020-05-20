# global variable
a = 10


def something():
    # local variable
    a = 15
    x = globals()['a']
    print 'in side function', a
    print 'in side function', x
    globals()['a'] = 20


something()
print a

lst = [10, 12, 13, 14, 15, 16, 17, 18]

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = count(lst)

print ('Even : {} and Odd : {} '.format(even, odd))
