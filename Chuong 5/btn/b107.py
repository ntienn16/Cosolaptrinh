list=[]
while True:
    n=input()
    if n not in list:
        list=list+[n]
    if n=="" or n==" ":
        break

for a in range (len(list)):
    print(list[a])