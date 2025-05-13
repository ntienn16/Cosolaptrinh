def nhap():
    L=[]
    n=int(input("n="))
    for a in range (n):
        a=int(input())
        L=L+[a]
    x=int(input("x="))
    return n,x,L
def firstandlast(L):
    print(L[:1]+L[(len(L)-1):])
    return
def search(L,x):
    if x in L: print("True")
    else: print("False")
    return
n,x,L=nhap()
firstandlast(L)
search(L,x)