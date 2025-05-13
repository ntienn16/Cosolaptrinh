def nhap():
    thongtin=input()
    return thongtin
def email(thongtin):
    email = ""
    if "Email:" in thongtin:
        email = thongtin.split("Email:")[1].strip()
    print(email)
thongtin=nhap()
email(thongtin)