def nhap():
    n=int(input("n="))
    return n

def inkq(n):
        for i in range(1,n+1):
            if  i%2==0:
                print(i,end=" ")

while True:
    n=nhap()
    inkq(n)
    tt=input("\nTiep tuc khong?")
    if tt=="k" or tt=="K":
        break