while True: 
    nguoi=int(input())
    if nguoi!=0 and 1<=nguoi<=3:
        import random
        def dapan(answerNumber):
            if answerNumber ==1:  
                return "1"
            elif answerNumber ==2:
                return "2"
            elif answerNumber ==3:
                return "3"
        r=random.randint(1,3)
        may=dapan(r)
        print(may)
        if may=="1":
            if nguoi==1:
                print("Hoa")
            elif nguoi==2:
                print("May thang")
            else:
                print("Nguoi thang")
        elif may=="2":
            if nguoi==1:
                print("Nguoi thang")
            elif nguoi==2:
                print("Hoa")
            else:
                print("May thang")
        elif may=="3":
            if nguoi==1:
                print("May thang")
            elif nguoi==2:
                print("Nguoi thang")
            else:
                print("Hoa")
    elif nguoi==0:
        break