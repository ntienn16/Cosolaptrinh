def nhap():
    n=input()
    return n
def test(n):
    n=n.split(",")
    chia3=[]
    for a in n:
        b=int(a,2)
        if b%3==0:
            chia3.append(a)
    return ",".join(chia3)
n=nhap()
print(test(n))