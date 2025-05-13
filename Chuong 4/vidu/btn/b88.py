def nhap():
    a=float(input("Chiều dài ống hút a:"))
    b=float(input("Chiều dài ống hút b:"))
    c=float(input("Chiều dài ống hút c:"))
    return a,b,c
def ktra(a,b,c):
    if a<b+c and b<a+c and c<b+c:
        return True
    else: return False
a,b,c=nhap()
n=ktra(a,b,c)
if n==True:
    print("3 ống hút tạo thành tam giác")
else: print("3 ống hút không tạo thành tam giác")