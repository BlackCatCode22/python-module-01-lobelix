# Compute gross pay
def computepay(hours, rate):
    if hours > 40:
        print("\n" + "Overtime")
        ot_rate = rate * 0.5
        ot_hours = hours - 40
        regular_pay = rate * hours
        overtime_pay = ot_hours * ot_rate
        gross_pay = regular_pay + overtime_pay

        # alternatively

        # ot_rate = rate * 1.5
        # ot_hours = hours - 40
        # overtime_pay = ot_hours * ot_rate
        # gross_pay = 40 * rate + overtime_pay
    else:
        print("\n" + "Regular")
        gross_pay = rate * hours
    return gross_pay
# Enter the hours
# Check the validity of the input
hours = input("Enter hours: ")
try:
    hours = float(hours)
except ValueError:
    print("Error, please enter numeric input")
    quit()
# Enter the rate
# Check the validity of the input
rate = input("Enter rate: ")
try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric input")
    quit()
# Compute the pay
gross_pay = computepay(hours, rate)
print("Gross Pay =", gross_pay)