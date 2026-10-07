#wap the amstrong progam

def armstrong(num):
    x = 0
    for i in str(num):
        x += int(i)**3
    if x == num:
        return True
    else:
        return False

print(armstrong(153))

#Explain the progarm 
#with some simple words
'''
  for i in num:
        x += i**3

    expine the for loop and the else block 
    the for loop is used to iterate over a sequence 
    the else block is used to print the message when the loop is terminated successfully
    the break statement is used to break the loop
    the continue statement is used to continue the loop  
'''
