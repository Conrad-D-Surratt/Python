user_input = float(input("\nEnter an integer: "))
user_input_two = float(input("Enter another integer: ")) #I'm not trusting the user to enter an integer.
print()
int_one = int(user_input)
int_two = int(user_input_two) #Converts the floats into integers.
if int_one > 0 and int_two > 0:
    print("Both numbers are greater than 0")
if int_one > 100 and int_two > 100:
    print("Both numbers are greater than 100") #Two and statements.
if int_one % 2 == 0 or int_two % 2 == 0:
    print("At least one number is even")
if int_one < 100 or int_two < 100:
    print("At least one of the numbers is less than 100") #Two or statements.
if not int_one == int_two:
    print("The numbers are not equal")
if not int_one == 0:
    print("The first number is not zero") #Two not statements.
print()
#A couple of blank lines for visual clarity. This was a fun one to figure out!