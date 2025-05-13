def Input():
    L=[]
    n=int(input("n="))
    for a in range (n):
        a=int(input())
        L=L+[a]
    return L
def Search(L):
    max=L[0]
    min=L[0]
    for i in range (len(L)):
        if L[i]>max:
            max=L[i]
        if L[i]<min:
            min=L[i]
    return max,min
def output(max,min):
    print(max,min)
    
L=Input()
max,min=Search(L)
output(max,min)