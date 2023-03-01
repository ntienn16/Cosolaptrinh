a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
min=a
if  max<=b:
    max=b
else:
    min=b
if  max<=c:
    max=c
else:
    min=c
print("SLN=",max,sep="")
print("SBN=",min,sep="")