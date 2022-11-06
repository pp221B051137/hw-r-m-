import itertools
def perm(n):
    add = []
    add2 = []
    val = range(1,n+1)
    perm_set = itertools.permutations(val)
    for i in (perm_set):
        add.append(i)
    for i in add:
        for j in range(1,len(i)):
            a,b = i[j-1],i[j]
            if abs(b-a) > 3 or i[0]!=1 or i[len(i)-1]!=len(i):
                break
        else:
            add2.append(i)
    return len(add2)
# n = int(input("n: ")) 
l = int(input("L: "))
cnt = 0    
for i in range(1,l+1):
    cnt+=perm(i)**3
# print("f(n) =",perm(n))
print("S(L) =",cnt)