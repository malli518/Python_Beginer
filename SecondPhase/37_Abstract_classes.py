from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print('This is laptop')


# com = Computer()
com = Laptop()
com.process()
