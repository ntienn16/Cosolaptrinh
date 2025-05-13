def nhap():
    n=input("Nhập chuỗi:")
    return n
def output(n):
    list=[]
    M=[]
    list=n.split()
    for dau in list:
        M=M+[dau.rstrip("\"-,.:;!'?")]
    print(M)
    
n=nhap()
output(n)