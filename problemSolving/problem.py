
def star(x,y):
    for i in range(x,y+1):
        for j in range(y):
            print("*", end=" ")
        print()

star(5,9)

def num(x,y):
    for i in range(x,y+1):
        for j in range(y):
            print(i, end=" ")
        print()

num(1,5)

def char(x,y):
    for i in range(x,y+1):
        for j in range(x,y+1):
            print(chr(j), end=" ")
        print()

char(ord(input("Enter the first character: ")),ord(input("Enter the last character: ")))


