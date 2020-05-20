def greet():
    print 'Hello',
    print 'World'


def add(x, y):
    c = x + y
    d = x - y
    return c, d


greet()
print add(40, 20)


def update(x):
    print id(x)
    x = 8
    print id(x)
    print 'x', x


a = 10
print id(a)
update(a)
print 'a', a

# in python there is not concept like pass by value or pass by reference
# list is immuetable


def update_list(lt):
    print id(lt)
    lt[1] = 25
    print id(lt)
    print lt


lst = [10, 20, 30]
print id(lst)
update_list(lst)
print lst

