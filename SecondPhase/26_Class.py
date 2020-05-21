class Computer:
    def config(self):
        print('1GB RAM 1TB HD')


com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()
