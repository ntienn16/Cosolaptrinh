print("$10.95 cho mặt hàng đầu tiền, cộng thêm $2.95 cho mỗi mặt hàng tiếp theo")
def sohang():
    n=int(input("Nhập số lượng hàng:"))
    return n
def tinhtien(n):
    tien=0
    if n==1:
        tien=10.95
    elif n>1:
        tien=10.95+(n-1)*2.95
    return tien
n=sohang()
tien=tinhtien(n)
print("Phí vận chuyển là:$",round(tien,2),sep="")