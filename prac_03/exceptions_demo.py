"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while numerator == 0 or denominator == 0:
        print("numerator or denominator cannot be set to zero.")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
#A ValueError will occur if a non integer number or a value that is not a number is entered.
#A ZeroDivisionError will occur if either the numerater or the denominator are set to zero.
# A while loop can be used to error check that neither the denominator nor the numerator are set to zero

