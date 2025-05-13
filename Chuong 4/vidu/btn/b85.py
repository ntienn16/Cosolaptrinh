def nhap():
    n=int(input("n="))
    return n
def ordinal(n):
    if n==1:
        return "First"
    elif n==2:
        return "Second"
    elif n==3:
        return "Third"
    elif n==4:
        return "Fourth"
    elif n==5:
        return "Fifth"
    elif n==6:
        return "Sixth"
    elif n==7:
        return "Seventh"
    elif n==8:
        return "Eighth"
    elif n==9:
        return "Ninth"
    elif n==10:
        return "Tenth"
    elif n==11:
        return "Eleventh"
    elif n==12:
        return "Twelfth"
    else:
        return ""
n=nhap()
print(ordinal(n))