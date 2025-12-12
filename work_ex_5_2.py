# Initialize an empty list to store numbers
numbers = []

# Read numbers until a blank line is entered
while True:
    # Prompt the user to enter a number or 'done'
    user_input = input("Enter a number or 'done' to finish: ")

    # Check if the user entered done to break the loop
    if user_input == 'done':
        break
    try:
        # Try to convert the input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        # If conversion fails, notify the user and continue the loop
        print("Invalid input. Please enter a numeric value or 'done' to finish.")

# Check if the list is not empty before finding the maximum and minimum
if numbers:
    maximum = max(numbers)
    minimum = min(numbers)
    print(f"\nMaximum number: {maximum}")
    print(f"Minimum number: {minimum}")
else:
    print("No numbers were entered.")
