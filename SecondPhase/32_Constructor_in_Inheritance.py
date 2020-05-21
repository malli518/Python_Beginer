class A:
    def __init__(self):
        print('Init A Constructor ')

    def function1(self):
        print('Function 1 working ')

    def function2(self):
        print('Function 2 working')


class B:
    def __init__(self):
        print('Init B Constructor')

    def function3(self):
        print('Function 3 working ')

    def function4(self):
        print('Function 4 working')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('Init C Constructor')

    def function3(self):
        print('Function 3 working ')

    def function4(self):
        print('Function 4 working')


class D(A):
    def __init__(self):
        # super(D, self).__init__()
        super().__init__()
        print('Init D Constructor')


c = C()
d = D()

print('In Python Constructor() will participate in Inheritance')
# In Python Constructor will participate in Inheritance
# if you create a object of sub class it will first try to find init of sub class
# if it is not found then it will call init of super class
# MRO (Method Resolution Order ) the order should be left to right while calling super Constructor, means
# if a class inherits two classes first it will check child class methods or Constructor and if it is not
# present then it will check left class methods or Constructor here the left class is 'A' then
# it will check right class methods or Constructor here the right class is 'B'
# same thing will applicable for methods as well
