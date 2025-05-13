def pheptoan(left, right, dau):
	if dau == "+": return left + right
	if dau == "-": return left - right
	if dau == "*": return left * right
	if dau == "/": return left / right
	if dau == "^": return left ** right
def main(postfix):
    vals=[]
    for token in postfix:
        if (token).isnumeric():
            vals.append(int(token))
        else:
            right=vals.pop()
            left=vals.pop()
            vals.append(pheptoan(left,right,token))
            print(left)
            print(right)
        print(vals)
postfix=input("Nhập:")
main(postfix)