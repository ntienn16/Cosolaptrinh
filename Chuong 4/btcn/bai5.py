def LaSoNguyenTo(x):
    snt=0
    for i in range(1,x+1):
        if x%i==0:
            snt=snt+1
    if snt == 2:
        return True
    return False
def SoHopLe(x):
    if x<=1:
        return True
    return False
def NhapvaDem():
    print("Nhap day so:")
    x=int(input())
    kq=0
    while True:
        if (SoHopLe(x))==True:
            break
        else:
            if(LaSoNguyenTo(x))==True:
                kq=kq+1
            x=int(input())
    return kq

def InKQ(kq):
    print("Co",kq,"so nguyen to") 
kq=NhapvaDem()
InKQ(kq)