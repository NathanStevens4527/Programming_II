"""
Program using menu loop and functions for menu options
"""
MENU = "(P)rint stars\n(G)et result\n(Q)uit"

def main():
    score = int(input("Enter score: "))
    print(MENU)
    choice = input(">>> ")
    while choice != "Q":
        if choice == "P":
            print_stars(score)
        elif choice == "G":
            result = determine_result(score)
            print(result)
        else:
            print("Invalid choice")
        choice = input("\n>>> ")
    print("Goodbye")

def determine_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    for i in range(0, score):
        print("*", sep="", end="")

main()