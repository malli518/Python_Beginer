def person(name, age=18):
    print(name)
    print(age)


person('Nag', 27)
person(age=27, name='nagamalli')
person('Ram')


def add(a, b):
    print(a + b)


print(add(10, 20))


# variable length like vargs in java


def add1(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)


add1(10, 20, 30, 40)

# keyword variable length arguments


def person1(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


person1('Nag', age=27, city='Hyd', mobile=9553583771)
