class TopTen:

    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def next(self):
        if self.count <= 10:
            value = self.count
            self.count += 1
            return value
        else:
            raise StopIteration


values = TopTen()
itr = values.__iter__()
print itr.next()
print itr.next()
print itr.next()
# for i in values:
#     print i



