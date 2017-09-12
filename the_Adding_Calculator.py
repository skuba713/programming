#The Adding Calculator
#r/dailyprogrammer challenge #331 [Easy]
#Make a calculator that lets the user add, subtract, multiply and divide integers. It should allow exponents too.
#The user can only enter integers and must expect the result to be integers.
#The twist is that YOU, the programmer, can only let the program calculate expressions using addition.

#Addition
def add(num1,num2):
    new_num = num1 + num2
    return new_num

#Multiplication
def multiply(num1,num2):
    i=0
    new_num = 0
    if num1 <= num2:
        while i < num1: #issue with negative numbers
            new_num += num2
            i += 1
    else:
        while i < num2:
            new_num += num1
            i +=1
    return new_num

#Exponents
def exponent(num1,num2):        # num1^num2
    i = 1
    new_num=num1
    while i < num2:
        print(new_num)
        new_num = multiply(new_num,num1)
        i +=1
        print(new_num)
        
    if num2 == 0:
        new_num = 1
    #if num1 == -1:
        #new_num = -1
    if num2<-1 and num1 != -1:
        new_num = "Non-integral answer"
    if num1 == 0 and num2<-1:
        new_num = "Not-defined"
    return new_num

#Subtraction


#Division

        
    

num1 = int(input("What is the first number?\n"))
num2 = int(input("What is the second number?\n"))

new_num = add(num1,num2)
print(new_num)

new_num = multiply(num1,num2)
print(new_num)

new_num = exponent(num1,num2)
print(new_num)

