toan=int(input())
ly=int(input())
hoa=int(input())
dtb=(toan*2+ly*3+hoa)/6
if  dtb<3:
    print("Kem")
if  3<=dtb<5:
    print("Yeu")
if  5<=dtb<6:
    print("Trung binh")
if  6<=dtb<7:
    print("Trung binh kha")
if  7<=dtb<8:
    print("Kha")
if  8<=dtb<9:
    print("Gioi")
if  9<=dtb<10:
    print("Xuat sac")