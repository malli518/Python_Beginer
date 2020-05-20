file = open('data.txt', 'r')
print file.readline()
print file.readline()
# print file.read()

file1 = open('abc.txt', 'w')
# file1.write(file.read())
file2 = open('ab.txt', 'a')
file2.write(file.read())
file4 = open('image.jpg', 'wb')

