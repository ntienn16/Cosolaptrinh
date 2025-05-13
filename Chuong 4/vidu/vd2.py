def Nhap():
    n = int(input("Nhập số nguyên n: "))
    count = 0
    for i in range(n):
        x = int(input())
        if x % 2 == 0:
            count += 1
    return count

def NhapVaDem(n):
    count = 0
    for i in range(n):
        x = int(input())
        if x % 2 == 0:
            count += 1
    return count

def InKQ(kq):
    print("Số lượng chữ số chẵn đã được nhập vào là:", kq)
n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)