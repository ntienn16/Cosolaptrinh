def nhap():
    uocso=[]
    tong=0
    n=int(input("Nhập số n:"))
    for i in range (1,n):
        if n%i==0:
            uocso=uocso+[i]
            tong=tong+i
    return (n,uocso,tong)
def perfect(n,uocso,tong):
    print("Ước số của",n,"là:",end=" ")
    if tong==n:
        for a in range(len(uocso)):
            print(uocso[a],end=" ")
        print()
        print(n,"là số hoàn hảo")
    else:
        for b in range(len(uocso)):
            print(uocso[b],end=" ")
        print()
        print(n,"không phải là số hoàn hảo")

n,uocso,tong=nhap()
perfect(n,uocso,tong)