def fact(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    print(result)


n = int(input('Enter a number'))
fact(n)
