# Compute gross pay
hours = input("Enter hours: ")
rate = input("Enter rate: ")
hours = float(hours)
rate = float(rate)
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
print("Gross Pay =", gross_pay)