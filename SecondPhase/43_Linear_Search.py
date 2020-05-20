pos = -1


def search(list, n):
    count = 0
    for i in list:
        if i == n:
            globals()['pos'] = count
            return True
        count += 1
    return False


list = [1, 2, 3, 4, 5, 6]
n = 6

if search(list, n):
    print 'Found at', pos
else:
    print 'Not Found'
