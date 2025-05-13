def inhoa(chuoi):
    chuoi = chuoi.capitalize()
    for i in range(len(chuoi)):
        if chuoi[i] == '.' or chuoi[i] == '!' or chuoi[i] == '?':
            j = i + 1
            while j < len(chuoi) and chuoi[j] == ' ':
                j += 1
            if j < len(chuoi):
                chuoi = chuoi[:j] + chuoi[j].upper() + chuoi[j+1:]
        elif chuoi[i] == 'i':
            if (i == 0 or chuoi[i-1] == ' ') and (i+1 == len(chuoi) or chuoi[i+1] == ' '):
                chuoi = chuoi[:i] + 'I' + chuoi[i+1:]
    return chuoi

chuoi = input("Nhap chuoi: ")
print(inhoa(chuoi))