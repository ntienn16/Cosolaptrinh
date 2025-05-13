n=input()
n=n.split(",")
L=[]
for i in n:
    if i not in L:
        L.append(i)
L.sort()
print(",".join(L))