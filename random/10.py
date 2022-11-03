import random

upper = 'ABCDEFJHIGKLMNOPQRSTUVWXYZ'
lower = 'abcdefjhigklmnopqrstuvwxyz'
num = '1234567890'
number = [4,5,6,7,8,9,10]
add = []
add_2 =[]
main =[]
all = upper+lower
for i in all:
    add.append(i)
for j in num:
    add_2.append(j)

n = random.choice(number)
n2 = 10-int(n)
a = random.choices(add,k=n2)
b = random.choices(add_2,k=n)
for i in a:
    main.append(i)
for j in b:
    main.append(j)
for m in main:
    print(m,end="")