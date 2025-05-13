def nhap():
    uocso=[]
    n=int(input("Nhập số n:"))
    for i in range (1,n):
        if n%i==0:
            uocso=uocso+[i]
    return (n,uocso)
def inkq(n,uocso):
    print("Ước số của",n,"là:",end=" ")
    for a in range (len(uocso)):
        print(uocso[a],end=" ")
        
n,uocso=nhap()
inkq(n,uocso)