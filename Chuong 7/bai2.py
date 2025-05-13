def nhap():
    n=input()
    return n
def fix(n): 
    n=n.strip()
    n=n.replace("  "," ").replace(" ,",",").replace(" .",".").replace(" :",":").replace(" ;",";")
    n=n.capitalize()
    print(n)
n=nhap()
fix(n)