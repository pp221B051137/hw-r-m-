import random
d = input()
n = int(input())
s = random.choices(d,k=n)
for i in s:
    print(i,end='')