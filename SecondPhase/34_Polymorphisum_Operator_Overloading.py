class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        return Student(m1, m2)

    def __gt__(self, other):
        a = self.m1 + self.m2
        b = other.m1 + other.m2
        if a > b:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(68, 50)
s2 = Student(50, 78)
# Student.__add__(s1, s2) here we are overloading + operator
s3 = s1 + s2
print(s3.m1)
# Student.__sub__(s1, s2) here we are overloading - operator
s4 = s1 - s2
print(s4.m1)
# Student.__gt__(s1, s2) here we are overloading > operator
if s1 > s2:
    print('S1 wins')
else:
    print('S2 wins')

x = 8
# here it is printing value not a object address
print(8)
# here it is printing address of s1 not values ( it is internally calling __str__ method )
print(s1)
print(s2)


