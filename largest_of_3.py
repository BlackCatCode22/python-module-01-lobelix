# Find the largest of 3 integers

# Enter the first integer
num1 = input("Enter the first integer: ")
try:
    num1 = int(num1)
except ValueError:
    print("Error, please enter an integer")
    quit()
# Enter the second integer
num2 = input("Enter the second integer: ")
try:
    num2 = int(num2)
except ValueError:
    print("Error, please enter an integer")
    quit()
# Enter the third integer
num3 = input("Enter the third integer: ")
try:
    num3 = int(num3)
except ValueError:
    print("Error, please enter an integer")
    quit()
# Find the largest integer
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print("\n" + "Largest integer =", largest)