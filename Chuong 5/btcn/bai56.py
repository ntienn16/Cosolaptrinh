def nhap():
    listA=[]
    for a in range(10):
        a=int(input())
        listA=listA+[a]
    return listA
def baitoan(listA):
    listB=[]
    for i in range (0,len(listA),2):
        listB=listB+[listA[i+1]]
        listB=listB+[listA[i]]
    for b in range (len(listB)):
        print(listB[b],end=" ")

listA=nhap()
baitoan(listA)