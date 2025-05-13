n=int(input("n="))
if  0<=n<=100:
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    print(str(n)+"!="+str(gt))