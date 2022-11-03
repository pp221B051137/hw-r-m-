import random
q = []
for n in range(1,6):
    q.append(n)
e = True
# count = 0
cnt = 0
s=[]
while e:
    d = str(input())
    w = random.choice(q)
    s.append(w)
    if cnt <= 4:
       cnt+=1
       print(s[0])
    else:
       print(w)
    if d == "0":
        e = False
    
