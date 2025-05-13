x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
if  ch== "+":
    print(str(x)+str(ch)+str(y)+"=",x+y,sep="")
elif    ch=="-":
    print(str(x)+str(ch)+str(y)+"=",x-y,sep="")
elif    ch=="*":
    print(str(x)+str(ch)+str(y)+"=",x*y,sep="")
elif    ch=="/":
    if  y==0:
        print("khong hop le")
    else:
        print(str(x)+str(ch)+str(y)+"=",x/y,sep="")
else:
    print("Khong hop le")
