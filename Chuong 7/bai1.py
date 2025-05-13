n=input()
inhoa=0
inthuong=0
chuso=0
khac=0
for i in n:
    if i.isupper():
        inhoa=inhoa+1
    elif i.islower():
        inthuong=inthuong+1
    elif i.isnumeric():
        chuso=chuso+1
    else:khac=khac+1
print("In hoa:",inhoa)
print("In thuong:",inthuong)
print("Chu so:",chuso)
print("Khac:",khac)