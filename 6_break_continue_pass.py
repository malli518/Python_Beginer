# break
x = int(input('Enter a number'))
i = 1
av = 5
while i <= x:
    if i > av:
        print('Out of stock')
        break
    print('Hello')
    i += 1
print('bye')
# continue
# print 1 to 100 and skip divisible bye 3

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# pass
for i in range(1, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)
