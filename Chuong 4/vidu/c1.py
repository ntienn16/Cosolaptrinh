def nhap():
    n=int(input("n="))
    return n
def nhapvadem(n):
    kq=0
    print("Nhap",n,"so nguyen")
    for i in range (1,n+1):
            x=int(input())
            if x!=0:
                if x%2==0:
                    kq=kq+1
    return kq
def inkq(kq):
    print("So chu so chan la:",kq)
    
n=nhap()
kq=nhapvadem(n)
inkq(kq)