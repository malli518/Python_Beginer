# Class Methods
# Instance Methods
# Static Methods


class Student:
    # class variables
    school = "ZPHSchool"
    # Constructor

    def __init__(self, m1, m2, m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance method (to work with instance variables ) -> it will take ref as a Class object

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class method is to work with class variables (static variables ) -> it will take ref as a Class

    @classmethod
    def get_school(cls):
        return cls.school

    # Static method which is not related to class variables and instance variables -> no need to pass any variables

    @staticmethod
    def info():
        print('this is a static method ')


std = Student(40, 60, 73)
print(std.avg())
print(Student.get_school())
print(Student.info())


