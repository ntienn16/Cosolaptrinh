def nhap():
    chuoi=input("Nhập chuỗi:")
    eng=chuoi.split()
    return chuoi,eng
def piglatin(eng):
    vowels="aeiouAEIOU"
    latin=[]
    for n in eng:
        if n[-1] in ",.?!":
            dau=n[-1]
            n=n[:-1]
        else:dau=""
        for a in range(len(n)):
            if n[0] in vowels:
                m=n+"way"
                break
            else:
                if n[a] in vowels:
                    if n[0].islower():
                        m=(n[a:]+n[:a]+"ay")
                    else:
                        n=n.lower()
                        First=n[a].upper()
                        m=First+n[a+1:]+n[:a]+"ay"
                        break
        m=m+dau
        latin.append(m)
    return latin
chuoi,eng=nhap()
latin=piglatin(eng)
print(latin)