def nhap():
    n=input()
    x=int(input())
    return n,x
def vitri(n,x):
    n=n.split()
    L=[]
    M=[]
    for i in n:
        L=L+[int(i)]
    for y in range(len(L)):
        if x==L[y]:
            M.append(y+1)
    for b in M:
        print(b)
n,x=nhap()
a=vitri(n,x)