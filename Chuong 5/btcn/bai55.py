def nhap():
    listA=[]
    global n
    n=int(input("n="))
    for a in range(n):
        a=int(input())
        listA=listA+[a]
    return listA
def baitoan(listA):
    tong=0
    for i in range (n):
        if i%2==1:
            tong=tong+listA[i]
    print("Tong=",tong,)
    
listA=nhap()
baitoan(listA)