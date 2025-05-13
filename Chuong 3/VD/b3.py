while True:
    n=int(input())
    for i in range (1,n+1):
        if i%2==0:
            print(i,end=" ")
    tt=input("Tiep tuc khong?")
    if tt=="K" or tt=="k":
        break