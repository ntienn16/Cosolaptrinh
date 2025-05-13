def isInteger(chuoi):
    chuoi=chuoi.strip()
    if len(chuoi)==0:
        return False
    if chuoi[0]=="+" or chuoi[0]=="-":
        chuoi=chuoi[1:]
    return chuoi.isdigit()
def pheptoan(left, right, toantu):
	if toantu == "+": return left + right
	if toantu == "-": return left - right
	if toantu == "*": return left * right
	if toantu == "/": return left / right
	if toantu == "^": return left ** right
def evalPostfix(postfix):
    eval=[]
    for token in postfix:
        if isInteger(token):
            eval.append(int(token))
        else:
            right=eval.pop()
            left=eval.pop()
            eval.append(pheptoan(left,right,token))
    return eval
def Postfix(chuoi):
    operators = []
    postfix = []
    for i in chuoi:
        if i == '(':
            operators.append(i)
        elif i == ')':
            while True:
                operator = operators.pop()
                if operator == '(':
                    break
                postfix.append(operator)
        elif i == '+' or i == '-':
            if len(operators) > 0 and (operators[-1] == "^" or '*' or '/'):
                while True:
                    operator = operators.pop()
                    if operator == '(':
                        operators.append(operator)
                        break
                    postfix.append(operator)
                    if operators == []:
                        break
            operators.append(i)
        elif i == '*' or i == '/':
            if len(operators) > 0 and (operators[-1] == "^"):
                while True:
                    operator = operators.pop()
                    if operator == '(':
                        operators.append(operator)
                        break
                    postfix.append(operator)
                    if operators == []:
                        break
            operators.append(i)
        elif i=="^":
            operators.append(i)
        else:
            postfix.append(i)
    while operators != []:
        postfix.append(operators.pop())
    return postfix
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
def main():
    chuoi=input("Nhập:")
    postfix=Postfix(tokenizing(chuoi))
    print(" ".join(postfix))
    eval=evalPostfix(postfix)
    print(eval)
main()