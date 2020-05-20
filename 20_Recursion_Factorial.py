def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


n = input('Enter a number')
result = fact(n)
print result
