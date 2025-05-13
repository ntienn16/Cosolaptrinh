while True:
    a=float(input("a="))
    b=float(input("b="))
    tt=input("Toan tu:")
    if  tt=="+" or  tt=="-" or tt=="*" or tt=="/":
        if(tt=="+"):
            print(a,"+",b,"=",a+b,sep='')
        elif(tt=="-"):
            print(a,"-",b,"=",a-b,sep='')
        elif(tt=="*"):
            print(a,"*",b,"=",a*b,sep='')
        elif(tt=="/" and b!=0):
            print(a,"/",b,"=",a/b,sep='')
    tiep=input("Tiep tuc:")
    if  tiep=="T" or tiep=="t":
        break