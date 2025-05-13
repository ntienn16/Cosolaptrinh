n=int(input("n="))
if  0<=n<=9999:
    cs=0
    for i in range (0,n+1):
        if  0<=n<=9:
            cs=1
        elif    10<=n<=99:
            cs=2
        elif    100<=n<=999:
            cs=3
        elif    1000<=n<=9999:
            cs=4
print(n,"co",cs,"chu so")