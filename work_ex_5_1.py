num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except ValueError:
        print("Invalid input")
        continue
    num = num + 1
    tot = tot + fval
msg = f"The Total is {tot}, the count is {num}, the average is {tot/num}."
print(msg)
