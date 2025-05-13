def nhap():
    listA=[]
    n=int(input("n="))
    for a in range(n):
        a=int(input())
        listA=listA+[a]
    return listA
def list(listA):
    listB=listA
    print(listB,)
    listC=listA
    listC.sort(reverse=False)
    print(listC)
    
listA=nhap()
list(listA)