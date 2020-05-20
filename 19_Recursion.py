import sys

print sys.getrecursionlimit()
sys.setrecursionlimit(10)
print sys.getrecursionlimit()
i = 0


def greet():
     global i
     i += 1
     print 'hello', i
     greet()


greet()
