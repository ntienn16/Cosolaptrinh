import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
if  (a+b)>c and (a+c)>c and (b+c)>a:
    print("Dien tich=",round(dt,3),sep="")
else:
    print("Khong hop le")