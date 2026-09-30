


# Sudent=[]



# for i in range(10):
#     name = input("Enter the Student Name ")
#     Sudent.append(name)
    
# print(Sudent)

    

# p=[]

# while(len(p)<10):
#     a = input("Enter the city name :")
#     p.append(a)

# print(p)
# 5 byt 5 star pattner

'''
*****
*****
*****
# *****'''

# n= int(input("enter the numnber"))

# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()



# def table(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end=" ")
#         print()
    

# n= int(input("enter the numnber"))
# table(n)


# def print_char_pattern(start, end):
    
#     for i in range(start, end+1):
#         for j in range(start, end+1):
#             print(chr(j), end=" ")
#         print()

# start_char = ord(input("Enter the first char: "))
# end_char = ord(input("Where to stop: "))

# print_char_pattern(start_char, end_char)



# def i (p,n,m):
#     for i in range(p,n+1):
#         for j in range(m):
#             print(chr(i), end=" ")
#         print()

# i(ord(input("Enter the first char: ")),ord(input("Where to stop: ")),int(input("Enter the number of rows: ")))

#right rightstar

# def rstar(n):
#     for i in range(n):
#         for j in range(i):
#             print("*",end=" ")
#         print()
    
# rstar(5)

# for i in range(5):
#     print(i *i )

# rows = int(input("Enter number of rows: "))


# lsit = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# index = 0

# for i in range(1,):  # 4 rows
#     for j in range(i):
#         print(lsit[index], end=" ")
#         index += 1
#     print()


# # 1  Collect prime numbers using for loop
primes = []
for num in range(2, 50):
    count = 0
    for k in range(1, num + 1):
        if num % k == 0:
            count += 1
    if count == 2:
        primes.append(num)

print(primes)

# 2. Print pattern using for loops

index = 0
for i in range(1, len(primes)):
    for j in range(i):
        if index < len(primes):
            print(primes[index], end=" ")
            index += 1
        else:
            break
    print()

