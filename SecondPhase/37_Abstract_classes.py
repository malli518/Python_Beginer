from abc import ABCMeta, abstractmethod


class Computer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print 'This is laptop'


# com = Computer()
com = Laptop()
com.process()
