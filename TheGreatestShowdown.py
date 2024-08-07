#Task 1: Identify the Greatest 
# Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among 
#  the three.  

numbers = input("Enter three numbers seperated by commas A, B, C,")
print("You've chosen" + numbers)
split_numbers = numbers.split(",")
A, B, C  = (split_numbers)
print("The value of A is:" + A)
print("The value of B is:" + B.strip())
print("The value of C is:" + C.strip())
if int(A) > int(B) and int(A) > int(C):
    print("The largest number is" + A)
elif int(B) > int(A) and int(B) > int(C):
    print("The largest number is" + B)
else:
    print("The largest number is" + C)   
#Task 2: Identify the Smallest Improve upon your code from Task 1 
# to also determine the smallest number among the three and print it out.
if int(A) < int(B) and int(A) < int(C):
    print("The smallest number is" + A)
elif int(B) < int(A) and int(B) < int(C):
    print("The smallest number is" + B)
else:
    print("The smallest number is" + C)    