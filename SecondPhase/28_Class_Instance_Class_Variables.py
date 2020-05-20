class Car:
    # if you defined any variables out side the init methods , those variables are called class variables
    wheels = 4

    # if you defined any variables inside the inti method, those variables are called instance variables
    def __init__(self):
        self.name = "BMW"
        self.mil = 10


car1 = Car()
car2 = Car()
car1.mil = 15
Car.wheels = 5
print car1.mil, car1.name, car1.wheels
print car2.mil, car2.name, car2.wheels
