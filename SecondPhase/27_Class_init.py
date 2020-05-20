class Computer:
    # it's like a constructor and it will execute only once when the object creation.
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print '1GB RAM 1TB HD', self.cpu, self.ram


com1 = Computer("i5", 16)
com2 = Computer("i7", 32)
com1.config()
com2.config()


class Computer1:
    def __init__(self):
        print 'inti'
        self.name = 'Nag'
        self.age = 27

    def compare(self, others):
        if self.age == others.age:
            return True
        else:
            return False


computer = Computer1()
computer.age = 26
computer1 = Computer1()
if computer.compare(computer1):
    print 'both objects are same'
else:
    print 'both objects are not same'

print computer.name
print computer1.name
