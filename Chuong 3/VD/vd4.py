while True:
    a=float(input("a="))
    b=float(input("b="))
    tt=input("Toan tu:")
    if  tt=="+":
        print(a,"+",b,"=",a+b,sep="")
    elif    tt=="-":
        print(a,"-",b,"=",a-b,sep="")
    elif    tt=="*":
        print(a,"*",b,"=",a*b,sep="")
    elif    tt=="/":
        print(a,"/",b,"=",a/b,sep="")
    else:print("Khong hop le")
    tiep=input("Tiep tuc:")
    if  tiep=="t" or tiep=="T":
        break