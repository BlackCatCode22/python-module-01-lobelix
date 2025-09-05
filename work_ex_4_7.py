# Scores reporting
def computegrade(score):
    if score < 0.0 or score > 1.0:
        print("Bad score")
        quit()
    else:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")

    # alternatively

    # if score >= 0.0 and score <= 1.0:
    #     if score >= 0.9:
    #         print("A")
    #     elif score >= 0.8:
    #         print("B")
    #     elif score >= 0.7:
    #         print("C")
    #     elif score >= 0.6:
    #         print("D")
    #     elif score < 0.6:
    #         print("F")
    # else:
    #     print("Bad score")

# Enter a score between 0.0 and 1.0
# Check the validity of the input
score = input("Enter score: ")
try:
    score = float(score)
except ValueError:
    print("Bad score")
    quit()
# Compute the grade
computegrade(score)