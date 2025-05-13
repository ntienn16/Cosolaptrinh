import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
if  (a+b)>c and (a+c)>b and (b+c)>a:
    print("Dien tich=",round(dt,3),sep="")
else:
    print("Khong hop le")