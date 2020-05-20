a = input('Enter a number ')
b = input('Enter b number ')


try:
    c = a / b
    print c
    x = input('Enter x number ')
    # y = int(x)
    # print y
except ZeroDivisionError as zde:
    print 'you con \'t divide by zero', zde
except NameError as ne:
    print 'please enter only integer ', ne
except Exception as e:
    print 'Unknown Exception ', e
finally:
    print 'Final block'

