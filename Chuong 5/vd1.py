def nhap():
    chuoi=input("Nhập chuỗi:")
    return chuoi
def infixtopostfix(chuoi):
    operators = []
    postfix = []
    dau={}
    dau["*"]=3
    dau["/"]=3
    dau["+"]=2
    dau["-"]=2
    dau["("]=1
    for c in chuoi:
        if c.isalnum():
            postfix.append(c)
        elif (c=="+" or c=="-") and chuoi[chuoi.index(c)-1]==" ":
            postfix
        elif c in dau:
            while len(operators) > 0 and operators[-1] != '(' and dau[(c)] <= dau[(operators[-1])]:
                postfix.append(operators.pop())
            operators.append(c)
        elif c == '(':
            operators.append(c)
        elif c == ')':
            while len(operators) > 0 and operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()
    while len(operators) > 0:
        postfix.append(operators.pop())
        
    return postfix
chuoi=nhap()
postfix=infixtopostfix(chuoi)
print(" ".join(postfix))