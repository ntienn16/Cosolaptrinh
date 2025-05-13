def nhap():
    chuoi=input("Nhập chuỗi:")
    chieurong=int(input("Độ rộng chuỗi:"))
    return chuoi,chieurong
def kq(chuoi,chieurong):
    if len(chuoi)>=chieurong:
        return chuoi
    space=(chieurong-len(chuoi))
    bentrai=space//2
    return " "*bentrai+chuoi

chuoi,chieurong=nhap()
kq=kq(chuoi,chieurong)
print(kq)