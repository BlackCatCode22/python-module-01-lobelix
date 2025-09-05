# Detailed output message to a user
# after finding the largest of 3 integers

def largest_of_3(num1, num2, num3):

    # Find the largest integer
    if num1 >= num2:
        if num1 >= num3:
            largest = num1
            max_num = "num1"
        else:
            largest = num3
            max_num = "num3"
    else:
        if num2 >= num3:
            largest = num2
            max_num = "num2"
        else:
            largest = num3
            max_num = "num3"

    # Message to user
    msg = (f"You entered 3 integers, {num1}, {num2}, and, {num3}.\n"
    f"The first integer you entered, {num1}, was assigned to a variable named, num1.\n"
    f"The second integer you entered, {num2}, was assigned to a variable named, num2, \n"
    f"and finally the third integer you entered, {num3}, was assigned to a variable named, num3. \n"
    f"Your input was processed and the largest number you entered was, {largest}, \n"
    f"which belonged to an integer variable named, {max_num}"
    )
    return msg

# Enter the first integer
num1 = input("Enter the first number: ")
try:
    num1 = int(num1)
except ValueError:
    print("Error, please enter an integer")
    quit()
# Enter the second integer
num2 = input("Enter the second number: ")
try:
    num2 = int(num2)
except ValueError:
    print("Error, please enter an integer")
    quit()
# Enter the third integer
num3 = input("Enter the third number: ")
try:
    num3 = int(num3)
except ValueError:
    print("Error, please enter an integer")
    quit()

#Output the message to user
display_msg = largest_of_3(num1, num2, num3)
print("\n" + display_msg)