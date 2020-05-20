class PyChram:
    def execute(self):
        print 'Compiling'
        print 'Running'


class MyEditor:

    def execute(self):
        print 'Spell Checking'
        print 'Naming convenstions'
        print 'Compiling'
        print 'Running'


class Laptop:
    # here ide is duck type
    def code(self, ide):
        ide.execute()


# ide = PyChram()
ide = MyEditor()
lap = Laptop()
lap.code(ide)


