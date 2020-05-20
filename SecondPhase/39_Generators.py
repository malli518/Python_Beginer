def topTen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def sqrtToTen():

    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topTen()
print values.next()
print values.next()
for i in values:
    print i

val = sqrtToTen()
for i in val:
    print i



