def nhap():
    n=input()
    return n
def matkhau(n):
    thuong=0
    so=0
    hoa=0
    dau=0
    if len(n)<6 or len(n)>17:
        return False
    elif len(n)>5 and len(n)<18:
        for i in n:
            if i.islower():
                thuong=thuong+1
            if i.isupper():
                hoa=hoa+1
            if i.isnumeric():
                so=so+1
            if i in "$#@":
                dau=dau+1
        if thuong>0 and hoa>0 and so>0 and dau>0:
            return True
        else:
            return False
n=nhap()
if matkhau(n)==True:
    print("True")
else:print("False")