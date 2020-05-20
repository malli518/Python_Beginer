from functools import reduce


def is_even(n):
    return n % 2 == 0


nums = [2, 4, 3, 6, 5, 1, 8, 7]
result = list(filter(is_even, nums))
print result


even = list(filter(lambda n: n % 2 == 0, nums))
print even

double = list(map(lambda n: n + n, even))
print double

sum1 = reduce(lambda a, b: a + b, double)
print sum1
