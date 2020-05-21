def div(a, b):
    print(a/b)


# Decorators -> you can change the behavior of the exiting function at the compile time
def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = smart_div(div)
div(4, 2)
