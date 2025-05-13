import math
def nhap():
    a=float(input("Độ dài cạnh a:"))
    b=float(input("Độ dài cạnh b:"))
    return a,b
def canhhuyen(a,b):
    c=math.sqrt(a**2+b**2)
    return c
a,b=nhap()
c=canhhuyen(a,b)
print("Độ dài cạnh huyền c:",c,sep="")