a=float(input())
b=float(input())
c=float(input())
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b and b==c and c==a:
        x='Tam giac deu'
    elif a*a==b*b+c*c or c*c==a*a+b*b or b*b==a*a+c*c:
        x='Tam giac vuong'
    else:x='Tam giac loai khac'
else:x='Khong hop le'
print(x)