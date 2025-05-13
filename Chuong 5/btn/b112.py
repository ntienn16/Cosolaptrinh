L=[]
tong=0
n=input
while True:
    n=(input())
    if n=="" or n==" ":
        break
    L=L+[float(n)]
    tong=tong+float(n)
trungbinh=tong/len(L)
print("Trung bình:"+str(trungbinh))
duoitb=[]
bangtb=[]
trentb=[]
for i in L:
    if i<trungbinh:
        duoitb=duoitb+[i]
    elif i==trungbinh:
        bangtb=bangtb+[i]
    else:trentb=trentb+[i]
print("Dưới trung bình:",end="")
for a in range(len(duoitb)):
    print(duoitb[a],end=" ")
print("\nBằng trung bình:",end="")
for b in range(len(bangtb)):
    print(bangtb[b],end=" ")
print("\nTrên trung bình:",end="")
for c in range(len(trentb)):
    print(trentb[c],end=" ")