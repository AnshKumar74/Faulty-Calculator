#Faulty Calculator
"""Design a calculator which will correctly solve all the problems except
the following ones:
       45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4"""
""" Your program should take operator and the two numbers as input from the 
user and then return the result"""
print("Enter a value(+ , - ,*, /):")
op = input() 
print("enter your value")
A = int(input())
print("enter your value")
B = int(input())
#addition
if op == "+":
    if A == 56 and B == 9 or A == 9 and B == 56 :
        print("77")
    else : 
        print("your value is" , A + B) 
 

 #multiplication
if op == "*":
    if A == 45 and B == 3 or A == 3 and B == 45 :
        print("555")
    else : 
        print("your value is" , A * B)
 
 #division
if op == "/":
    if A == 56 and B == 6 or A == 6 and B == 56 :
        print("4")
    else : 
        print("your value is" , A / B)
    
