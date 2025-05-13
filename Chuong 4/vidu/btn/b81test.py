import math
def tinhcanhhuyen(a,b):
    c=math.sqrt(a*a+b*b)
    return c
def main():
    a=float(input("Do dai canh a:"))
    b=float(input("Do dai canh b:"))
    c=tinhcanhhuyen(a,b)
    print("Do dai canh huyen c:",c,sep="")
main()