# #wap to print the 1 to 1000 prime number 


# def print_prime(start,end):
#     for i in range(start,end+1):
#         y=0
#         for j in range(2,i):
#             if i%j==0:
#                 y=1
#                 break
#         if y==0:
#             print(i)

# print_prime(1,1000)

   
# #wap to cal GCD 
# def gcd(a, b):
#   # Euclidean Algorithm (Iterative)
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(30,10))


#wap to lcm 
def lcm(a, b):
    #(// it give the floting value in python and  nume make it 
    # using the formula euclidid algorithm in python programming language 
    #Explin the alogirith and  thier output when i e
    #expin for and lcm
    ''' for loop it is used to iterate over a sequence 
    
    the syntax is as follows:
    for i in range(start,end+1):
        print(i)
    in this we  can also use the break and continue statements 
    the break statement is used to break the loop
    the continue statement is used to continue the loop
    when we use else with for loop it is used to print the message 
    when the loop is terminated successfully
    '''

    for i in range(1,a*b+1):
        if i%a == 0 and i%b == 0:
            return i

print(lcm(20,15))