def nhap():
    chuoi=input("Nhập chuỗi:").lower()
    eng=chuoi.split()
    return chuoi,eng
def piglatin(eng):
    vowels="aeiou"
    latin=[]
    for n in eng:
        for a in range(len(n)):
            if n[0] in vowels:
                latin.append(n+"way")
                break
            else:
                if n[a] in vowels:
                        latin.append(n[a:]+n[:a]+"ay")
                        break
    return latin
chuoi,eng=nhap()
latin=piglatin(eng)
print(latin)