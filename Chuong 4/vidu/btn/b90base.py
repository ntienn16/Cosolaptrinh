def isInteger(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in "+-":
        return s[1:].isdigit()
    return s.isdigit()
if __name__ == '__main__':
    s = input("Enter a string: ")
    if isInteger(s):
        print(f"{s} represents an integer.")
    else:
        print(f"{s} does not represent an integer.")