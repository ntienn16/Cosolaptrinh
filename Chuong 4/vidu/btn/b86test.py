def lyric(n):
    ordinal=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gift=["a partridge in a pear tree.", "two turtle doves,", "three French hens,", "four calling birds,", "five golden rings,", "six geese a-laying,", "seven swans a-swimming,", "eight maids a-milking,", "nine ladies dancing,", "ten lords a-leaping,", "eleven pipers piping,", "twelve drummers drumming,"]
    print(f"On the {ordinal[n - 1]} day of Christmas\nmy true love sent to me:")
    for i in range(n - 1, -1, -1):
        if i == 0 and n != 1:
            print("and", end=" ")
        print(gift[i])
    print()

def main():
    n=int(input("Nhap n:"))
    for i in range(1,n+1):
        lyric(i)
main()