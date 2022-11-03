import random
given = input()
add = []
add2 = []
try:
    for i in given:
        if i not in "0123456789.-+/.,=-?><!@#$%^&*()_":
            add2.append(i)
    a = random.choices(add2,k=5)
    for i in a:
        print(i,end="")
except:
    print("there is no string")