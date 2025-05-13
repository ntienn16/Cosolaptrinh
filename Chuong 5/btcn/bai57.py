def nhap():
    L=[]
    n=int(input("n="))
    for a in range (n):
        a=int(input())
        L.append(a)
    return L
def baitoan(L):
    M=[]
    for i in range (len(L)):
        if L[i] not in M:
            M=M+[L[i]]
    for b in range (len(M)):
        print(M[b],end=" ")
    
L=nhap()
baitoan(L)