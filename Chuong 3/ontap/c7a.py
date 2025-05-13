n=int(input("n="))
if  n<0 or n>100:
    print("Nhap lai n")
else:
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    print(str(n)+"!="+str(gt))