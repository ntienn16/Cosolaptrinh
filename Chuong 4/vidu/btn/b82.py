coban=4.00
print("Giá cơ bản:$4")
them=0.25/140
print("Cộng thêm:$0.25/140m")
def khoangcach():
    km=float(input("Khoảng cách đi được:"))
    return km
def tinhtien(km):
    m=km*1000
    tien=coban+(m*them)
    return tien

km=khoangcach()
tien=tinhtien(km)
print("Chuyến đi "+str(km)+" có giá tiền là:$"+str(round(tien,2)),sep="")