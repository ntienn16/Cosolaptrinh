import re
def nhap():
    password=input()
    return password
def matkhau(password):
    if len(password) < 6 or len(password) > 17:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[@#$]", password):
        return False
    else:return True
password=nhap()
print(matkhau(password))