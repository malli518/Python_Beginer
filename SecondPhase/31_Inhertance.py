class A:
    def function1(self):
        print('Function 1 working ')

    def function2(self):
        print('Function 2 working')

# Inheritance syntax:: Child_Class(Parent_Class) - > Single Inheritance


class B(A):
    def function3(self):
        print('Function 3 working ')

    def function4(self):
        print('Function 4 working')

# Inheritance syntax:: Child_Class(Parent_Class) - > Multi Level Inheritance


class C(B):
    def function5(self):
        print('Function 5 working ')

    def function6(self):
        print('Function 6 working')


class D:
    def function7(self):
        print('Function 7 working ')

    def function8(self):
        print('Function 8 working')

# Inheritance syntax:: Child_Class(Parent_Class1, Parent_Class2) - > Multiple Inheritance


class E(A, D):
    def function9(self):
        print('Function 9 working ')

    def function10(self):
        print('Function 10 working')


a = A()
a.function1()
a.function2()
print('########## Single Inheritance #############')
b = B()
b.function3()
b.function4()
b.function1()
b.function2()
print('########### Multi Level  Inheritance##############')
c = C()
c.function1()
c.function2()
c.function3()
c.function4()
c.function5()
c.function6()
print('########### Multiple  Inheritance##############')
e = E()
e.function1()
e.function2()
e.function7()
e.function8()
e.function9()
e.function10()

