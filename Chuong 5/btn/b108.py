am=[]
khong=[]
duong=[]
m=input()
while m!="":
    n=int(m)
    if n<0:
        am=am+[n]
    elif n==0:
        khong=khong+[n]
    elif n>0:
        duong=duong+[n]
    m=input()
for x in range (len(am)):
    print(am[x],end=" ")
for y in range (len(khong)):
    print(khong[y],end=" ")
for z in range (len(duong)):
    print(duong[z],end=" ")