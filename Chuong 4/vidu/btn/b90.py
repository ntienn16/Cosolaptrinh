def nhap():
    chuoi=input("Nhập chuỗi:")
    return chuoi
def isInteger(chuoi):
    chuoi=chuoi.strip()
    if len(chuoi)==0:
        return False
    if chuoi[0]=="+" or chuoi[0]=="-":
        chuoi=chuoi[1:]
    return chuoi.isdigit()
def inkq(chuoi):
    if isInteger(chuoi)==True:
        print("Chuỗi",chuoi, "là số nguyên")
    else:print("Chuỗi",chuoi,"không là số nguyên")

chuoi=nhap()
inkq(chuoi)