import random

add = []
for i in range(10,99):
    if i%5 == 0:
        r = i
        add.append(r)
e = random.choices(add,k=3)
print(e)