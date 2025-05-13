def nhap():
    n=int(input("Nhập ngày:"))
    return n
def day(n):
    ordinal=("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
    return f"On the day {ordinal[n-1]} of Christmas"
def lyric(n):
    gift=("a partridge in a pear tree.", "two turtle doves,", "three French hens,", "four calling birds,", "five golden rings,", "six geese a-laying,", "seven swans a-swimming,", "eight maids a-milking,", "nine ladies dancing,", "ten lords a-leaping,", "eleven pipers piping,", "twelve drummers drumming,")
    print(day(n),"\nmy true love gave to me:")
    for i in range(n, 0, -1):
        if i==1 and  n!=1:
            print("and", end=" ")
        print(gift[i-1])
    print()

def inkq(n):
    for i in range (1,n+1):
        lyric(i)

n=nhap()
inkq(n)