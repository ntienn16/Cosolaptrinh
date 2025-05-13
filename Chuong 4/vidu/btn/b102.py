def nhap():
    print("C là cup, TB là tablespoon, TE là teaspoon")
    dv=input("Nhập loại: ")
    n=int(input("Nhập số lượng:"))
    return dv,n
def quydoi(dv,n):
    if dv=="C" or dv=="c":
        c=n
        tb=0
        te=0
    elif dv=="tb" or dv=="TB" or dv=="tB" or dv=="Tb":
        c=n//16
        tb=n-(c*16)
        te=0
    elif dv=="te" or dv=="TE" or dv=="Te" or dv=="tE":
        c=n//48
        thua=n-c*48
        if thua<3:
            te=thua
            tb=0
        else:
            tb=(thua)//3
            te=thua-(tb*3)
    return c,tb,te
def intype(c,tb,te):
    if c==1:
        inc="cup"
    else:inc="cups"
    if tb==1:
        intb="tablespoon"
    else:intb="tablespoons"
    if te==1:
        inte="teaspoon"
    else:inte="teaspoons"
    return inc,intb,inte
def inkq(c,tb,te,inc,intb,inte):
    if c==0 and tb==0:
        print(te,inte)
    elif c==0 and te==0:
        print(tb,intb)
    elif tb==0 and te==0:
        print(c,inc)
    elif c==0:
        print(tb,intb +",",te,inte)
    elif tb==0:
        print(c,inc+",",te,inte)
    elif te==0:
        print(c,inc+",",tb,intb)
    else:print(c,inc+",",tb,intb+",",te,inte)
    
dv,n=nhap()
c,tb,te=quydoi(dv,n)
inc,intb,inte=intype(c,tb,te)
inkq(c,tb,te,inc,intb,inte)