a = int(input('Enter a number '))
b = int(input('Enter b number '))


try:
    c = a / b
    print(c)
    x = input('Enter x number ')
    y = int(x)
    print(y)
except ZeroDivisionError as zde:
    print('you con \'t divide by zero', zde)
except NameError as ne:
    print('please enter only integer ', ne)
except ValueError as ve:
    print('Please enter only integer values ', ve)
except Exception as e:
    print(e)
finally:
    print('Final block')

