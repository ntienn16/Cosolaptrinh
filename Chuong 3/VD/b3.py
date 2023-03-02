tt=int(input("Tieu thu="))
if  tt<=100:
    tien=tt*550
elif    tt<=150:
    tien=(100*550)+(tt-100)*750
elif    tt<=250:
    tien=(100*550)+(50*750)+(tt-150)*950
elif    tien<=201:
    tien=(100*550)+(50*750)+(50*950)+(tt-200)*1350
print("Phai tra=",tien+(tien*10)/100,sep="")