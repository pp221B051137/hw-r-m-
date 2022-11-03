import random
import string
n = int(input())
letters = string.ascii_lowercase
st = random.sample(letters, n)
for i in st:
    print(i,end="")