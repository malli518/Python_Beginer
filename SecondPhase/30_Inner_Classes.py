class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop('Lenovo', 'i7', 16)

    def show(self):
        print(self.name, self.roll_no)
        print(self.lap.show())

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


std = Student('Nag', 101)
std.show()
lap = Student.Laptop('Lenovo', 'i7', 16)
lap.show()
