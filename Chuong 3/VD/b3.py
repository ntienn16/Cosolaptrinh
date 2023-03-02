tt=int(input("Tieu thu="))
g1=550
g2=750
g3=950
g4=1350
if  tt<=100:
    tien=tt*g1
elif    tt<=150:
    tien=(100*g1)+(tt-100)*g2
elif    tt<=250:
    tien=(100*g1)+(50*g2)+(tt-150)*g3
else:
    tien=(100*g1)+(50*g2)+(50*g3)+(tt-200)*g4
print("Phai tra=",tien+(tien*10)/100,sep="")