import math
name=input("Ho ten: ")
snc=int(input("So ngay cong: "))
dg=int(input("Don gia ngay cong: "))
pc=float(input("He so phu cap: "))
tu=int(input("Tam ung: "))
luong=snc*dg*pc
tl=luong-tu
print("Nhan vien "+name+", Co tien Luong="+str(luong)+", Tam ung="+str(tu)+" va Thuc linh="+str(tl))