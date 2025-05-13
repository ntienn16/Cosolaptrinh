import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def giaipt(a,b,c):
    delta=(b*b)-4*a*c
    if delta<0:
        x1=x2=None
    elif delta==0:
        x1=x2=(-b)/(2*a)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
    return x1,x2
def inkq(x1,x2):
        if x1==x2==None:
            print("Phuong trinh vo nghiem")
        elif x1==x2==-b/(2*a):
            print("Phuong trinh co nghiem kep", "\n","x1=x2=",x1,sep="")
        else: print("Phuong trinh co hai nghiem","\n","x1="+str(x1),"\n","x2="+str(x2),sep="")

a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)