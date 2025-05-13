def nhap():
    n=int(input("n="))
    return n

def giaithua(n):
    x=1
    for i in range (1,n+1):
        x=x*i
    return x

def inkq(n,x):
    print(str(n)+"!="+str(x))

n=nhap()
gt=giaithua(n)
inkq(n,gt)