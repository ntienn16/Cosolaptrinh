n=input("acv i ca ica")
for i in range (len(n)):
    if n[i] == 'i':
        if (n[i-1] == ' ') and (n[i+1] == ' '):
            n = n[:i] + 'I' + n[i+1:]
print(n)