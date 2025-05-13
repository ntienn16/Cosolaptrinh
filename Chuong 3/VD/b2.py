while True:
    a=float(input("a="))
    b=float(input("b="))
    toantu=input("Toan tu:")
    if(toantu=="+"):
        print(a,"+",b,"=",a+b,sep='')
    elif(toantu=="-"):
        print(a,"-",b,"=",a-b,sep='')
    elif(toantu=="*"):
        print(a,"*",b,"=",a*b,sep='')
    elif(toantu=="/" and b!=0):
        print(a,"/",b,"=",a/b,sep='')
    else:print("Khong hop le")
    tieptuc=input("Tiep tuc:")
    if(tieptuc=="t" or tieptuc=="T"):break