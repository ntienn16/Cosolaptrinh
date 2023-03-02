import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if  (a+b)>c and (a+c)>b and (b+c)>a and a>0 and b>0 and c>0:
    if  a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print("Tam giac vuong")
    elif    a==b and b==c and c==a:
        print("Tam giac deu")
    else:
        print("Tam giac khac")
else:
    print("Khong hop le")