###                          ASSIGNMENT--->>1
###                  MODULE 2: BASIC PYTHON CONCEPTS





### TASK------>1  PERFORM BASIC MATHEMATICAL OPERATIONS

num1=float(input("Enter your first number: "))
num2=float(input("Enter your second name: "))

sum1 = num1 + num2
print(f"ADDITION: {sum1}")
difference = num1 - num2
print(f"SUBTRACTION: {difference}")
mult = num1 * num2
print(f"MULTIPLICATION: {mult}")
divide = num1 / num2
if num2 == 0:
    print("error.....")
else:
    divide = num1 / num2
    print(f"DIVISION: {divide}")








### TASK----->2   CREATE A PERSONALIZED GREETING

first_name = input("ENTER YOUR NAME: ")
second_name = input("ENTER YOUR LAST NAME: ")
full_name = first_name + " " +   second_name
#print(full_name)
print(f"HELLO {full_name}! WELCOME TO THE PYTHON WORLD!")



