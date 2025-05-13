def nhap():
    list=[]
    n=int(input("n="))
    for a in range (n):
        a=int(input())
        list=list+[a]
    return list
def snd(list):
    snd=0
    for i in range(len(list)):
        if list[i]>0:
            snd=snd+1
    return snd
def tbc(list):
    tong=0
    sohang=0
    tbc=0
    for i in range (len(list)):
        if list[i]%2==0:
            tong=tong+list[i]
            sohang=sohang+1
        if sohang==0:
            tbc=0
        else:tbc=tong/sohang
    return tbc
list=nhap()
snd=snd(list)
tbc=tbc(list)
print("SND="+str(snd))
print("TBC="+str(tbc))