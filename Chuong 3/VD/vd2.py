n=int(input("n="))
if  2<=n<=100:
    snt=0
    for i in range (1,n+1):
        if  n%i==0:
            snt=snt+1
    if  snt==2:
        print(n,"la SNT")
    else:
        print(n,"khong la SNT")
        