class Student:

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None :
            return a + b
        else:
            return a


st = Student()
# print st.sum(10, 20)
print(st.sum(10, 20))
