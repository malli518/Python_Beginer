def fib(n):
    a = 0
    b = 1
    if n < 0:
        print('Please enter positive number')
    elif n == 0:
        print('Please enter a number is more than zero')
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if c <= 100:
                print(c)
            else:
                break


n = int(input('Enter a number'))
fib(n)
