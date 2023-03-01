import math
a=float(input("Độ dài cạnh a:"))
b=float(input("Độ dài cạnh b:"))
c=float(input("Độ dài cạnh c:"))
S=(a+b+c)/2
print("Diện tích:",math.sqrt(S*(S-a)*(S-b)*(S-c)))