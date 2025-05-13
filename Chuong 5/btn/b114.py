import random
L=[]
while True:
    n=random.randint(1,49)
    if n not in L:
        L=L+[n]
    if len(L)==6:
        break
L.sort()
print(L)