def nhap():
    print("Nhập 3 số:")
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    return a,b,c
def trungvi(a,b,c):
    if a<=b<=c or c<=b<=a:
        return b
    elif a<=c<=b or b<=c<=a:
        return c
    else:return a
a,b,c=nhap()
tv=trungvi(a,b,c)
print("Trung vị của 3 số là:"+str(tv))