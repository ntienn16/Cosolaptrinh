def nhap():
    chuoi=input("Nhập chuỗi:")
    return chuoi
def inhoa(chuoi):
    chuoi=chuoi.capitalize()
    chuoi=chuoi.replace(" i "," I ")
    for a in range (len(chuoi)):
        if chuoi[a]=="." or chuoi[a]=="!" or chuoi[a]=="?":
            b=a+1
            while b<len(chuoi) and chuoi[b]==" ":
                b=b+1
            if b<len(chuoi):
                chuoi=chuoi[:b]+chuoi[b].upper()+chuoi[b+1:]
    return chuoi
chuoi=nhap()
print(inhoa(chuoi))