def nhap():
    L=[]
    while True:
        n=input("Nhập items:")
        if n=="" or n==" ":
            break
        L=L+[n]
    return L
def dinhdang(L):
    if len(L)==0:
        return None
    elif len(L)==1:
        return L[0]
    else: 
        return ", ".join(L[:-1])+" and "+L[-1]
L=nhap()
list=dinhdang(L)
print("Danh sách gồm:",list)