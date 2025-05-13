def nhap():
    chuoi=input("Nhap chuoi:")
    return chuoi
def tokenizing(chuoi):
    token=[]
    i=0
    while i<len(chuoi):
        if chuoi[i]==" ":
            i=i+1
            continue
        if chuoi[i] in ["^", "*", "/", "(", ")"]:
            token.append(chuoi[i])
            i=i+1
        elif chuoi[i]=="+" or chuoi[i]=="-":
            if i>0 and chuoi[i-1].isdigit() or chuoi[i-1]==")":
                token.append(chuoi[i])
                i=i+1
            else:
                num=chuoi[i]
                i=i+1
                while i<len(chuoi) and chuoi[i].isdigit():
                    num=num+chuoi[i]
                    i=i+1
                token.append(num)
        elif chuoi[i].isdigit():
            num=""
            while i<len(chuoi) and chuoi[i].isdigit():
                num=num+chuoi[i]
                i=i+1
            token.append(num)
        else:return[]
    return token
chuoi=nhap()
token=tokenizing(chuoi)
print(token)